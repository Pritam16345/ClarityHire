"""
agent.py — LangGraph graph assembly and ChromaDB initialization
The compiled app is the production artifact.

Usage:
    from agent import build_agent
    app, collection, embedder = build_agent()
    result = app.invoke({"question": "What is CTC?"}, config={"configurable": {"thread_id": "user_1"}})
"""

import os
import functools

# Load .env file if present (GROQ_API_KEY, etc.)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv optional; env vars can be set directly

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from sentence_transformers import SentenceTransformer
import chromadb

from state import ClarityContextState
from nodes import (
    user_context_manager,
    decision_engine_router,
    vector_fetcher,
    skip_vector_fetcher,
    calculator_action_step,
    llm_generator,
    reflection_grader,
    persist_checkpoint,
    choose_path_decision,
    grade_path_decision,
)
from knowledge_base.kb_documents import TEXTS, IDS, METADATAS


# ChromaDB + Embedder initialization

def init_knowledge_base():
    """
    Initialize SentenceTransformer embedder and ChromaDB collection.
    Verifies retrieval before returning.
    """
    print("📚 Loading SentenceTransformer embedder...")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    print("🗄️  Building ChromaDB knowledge base...")
    client = chromadb.Client()
    collection = client.create_collection(
        name="clarity_vector_db",
        metadata={"hnsw:space": "cosine"}
    )

    # Embed all documents
    embeddings = embedder.encode(TEXTS).tolist()

    collection.add(
        documents=TEXTS,
        embeddings=embeddings,
        ids=IDS,
        metadatas=METADATAS,
    )

    print(f"✅ Knowledge base built: {len(TEXTS)} documents indexed.")

Retrieval verification ──────────────────────────────────────────────
    print("\n🔍 Verifying retrieval...")
    test_queries = [
        ("What is CTC?", "CTC"),
        ("How is PF calculated?", "Provident Fund"),
        ("What is notice period?", "Notice Period"),
    ]
    all_passed = True
    for query, expected_topic in test_queries:
        q_emb = embedder.encode([query]).tolist()
        results = collection.query(query_embeddings=q_emb, n_results=1)
        top_topic = results["metadatas"][0][0].get("topic", "")
        passed = expected_topic.lower() in top_topic.lower()
        status = "✅" if passed else "⚠️ "
        print(f"  {status} '{query}' → '{top_topic}'")
        if not passed:
            all_passed = False

    if not all_passed:
        print("⚠️  Some retrieval tests failed. Review KB documents.")
    else:
        print("✅ All retrieval checks passed.\n")

    return collection, embedder


# Graph assembly

def build_agent():
    """
    Build and compile the LangGraph agent.
    Returns (compiled_app, collection, embedder).
    """
    collection, embedder = init_knowledge_base()

    # Inject collection and embedder into vector_fetcher via closure
    retrieval_with_deps = functools.partial(
        vector_fetcher,
        collection=collection,
        embedder=embedder
    )

Graph definition ────────────────────────────────────────────────────
    graph = StateGraph(ClarityContextState)

    # Add all nodes
    graph.add_node("memory", user_context_manager)
    graph.add_node("router", decision_engine_router)
    graph.add_node("retrieve", retrieval_with_deps)
    graph.add_node("skip", skip_vector_fetcher)
    graph.add_node("tool", calculator_action_step)
    graph.add_node("answer", llm_generator)
    graph.add_node("eval", reflection_grader)
    graph.add_node("save", persist_checkpoint)

    # Entry point
    graph.set_entry_point("memory")

    # Fixed edges
    graph.add_edge("memory", "router")
    graph.add_edge("retrieve", "answer")
    graph.add_edge("skip", "answer")
    graph.add_edge("tool", "answer")
    graph.add_edge("answer", "eval")
    graph.add_edge("save", END)

    # Conditional edges
    graph.add_conditional_edges(
        "router",
        choose_path_decision,
        {
            "retrieve": "retrieve",
            "skip": "skip",
            "tool": "tool",
        }
    )
    graph.add_conditional_edges(
        "eval",
        grade_path_decision,
        {
            "answer": "answer",  # retry
            "save": "save",      # accept
        }
    )

    # Compile with MemorySaver (multi-turn memory)
    app = graph.compile(checkpointer=MemorySaver())
    print("✅ Graph compiled successfully.\n")

    return app, collection, embedder


# Helper: run a single question

def ask(app, question: str, thread_id: str = "default") -> dict:
    """
    Invoke the agent with a question.
    MemorySaver restores all other state fields from checkpoint using thread_id.
    We only supply the new question + reset transient per-turn fields.
    Returns the full state dict.
    """
    config = {"configurable": {"thread_id": thread_id}}
    # Only pass fields that change each turn. MemorySaver restores:
    # messages, user_name, and any other persisted state from prior turns.
    initial_state = {
        "question": question,
        "route": "",
        "retrieved": "",
        "sources": [],
        "tool_result": "",
        "answer": "",
        "faithfulness": 0.0,
        "eval_retries": 0,
        "salary_inputs": {},
        "query_category": "",
        "follow_up_suggestions": [],
    }
    result = app.invoke(initial_state, config=config)
    return result
