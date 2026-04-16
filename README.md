# 📋 ClarityHire — Entry-Level Career Navigator

> An agentic RAG system built with LangGraph + ChromaDB that helps fresh graduates decode offer letters, calculate their real in-hand salary, and understand their legal rights as employees.

---

## 🎯 Problem Statement

**Domain:** Employment / HR Literacy  
**User:** First-time job seekers in India (fresh graduates, 0–2 years experience)  
**Problem:** Most fresh graduates sign their first offer letter without understanding PF, TDS, notice period clauses, or variable pay. They receive a ₹8 LPA offer and have no idea they'll take home ₹48,000/month — not ₹66,000.  
**Success:** A user can ask any question about their offer letter and receive a grounded, faithful answer sourced entirely from a verified knowledge base.  
**Tool:** CTC → In-Hand Salary Calculator (applies PF 12%, Professional Tax by state, TDS by regime)

---

## 🏗️ Architecture

```
User Question
    ↓
[user_context_manager] → sliding window (msgs[-6:]), name extraction, category classification
    ↓
[decision_engine_router] → LLM routing: retrieve | tool | memory_only
    ↓
[vector_fetcher]        [calculator_action_step]           [skip_node]
 ChromaDB top-3          CTC Calculator        Empty context
    ↓                        ↓                     ↓
                    [llm_generator] ← system prompt + grounding rules
                        ↓
                    [reflection_grader] → faithfulness score 0.0–1.0
                        ↓
             < 0.7 AND retries < 2 → retry llm_generator
             ≥ 0.7 OR max retries → persist_checkpoint → END
```

---

## ✅ Six Mandatory Capabilities

| # | Capability | Implementation |
|---|-----------|---------------|
| 1 | LangGraph StateGraph (3+ nodes) | 8 nodes: memory, router, retrieve, skip, tool, answer, eval, save |
| 2 | ChromaDB RAG (10+ docs) | 15 focused KB documents, 150–450 words each |
| 3 | MemorySaver + thread_id | Multi-turn memory with sliding window (msgs[-6:]) |
| 4 | Self-reflection eval node | Faithfulness scoring 0.0–1.0, threshold 0.7, max 2 retries |
| 5 | Non-trivial tool | CTC → In-Hand calculator: PF 12%, state PT, TDS by regime |
| 6 | Streamlit deployment | @st.cache_resource for LLM + ChromaDB, st.session_state for memory |

---

## 📚 Knowledge Base (15 Documents)

| ID | Topic |
|----|-------|
| doc_001 | CTC — What It Is and What It Includes |
| doc_002 | Basic Salary, HRA, and Special Allowance |
| doc_003 | Provident Fund (PF) — Complete Guide |
| doc_004 | TDS on Salary — How It Works |
| doc_005 | Professional Tax — State-Wise Rules |
| doc_006 | Gratuity — Eligibility and Calculation |
| doc_007 | Notice Period — What It Means |
| doc_008 | Probation Period — Rules and Implications |
| doc_009 | Variable Pay and Performance Bonus |
| doc_010 | Leave Policy — Types and Accrual Rules |
| doc_011 | ESOP and Joining Bonus — Clauses to Watch |
| doc_012 | Red Flags in an Offer Letter |
| doc_013 | Full and Final Settlement (F&F) |
| doc_014 | Background Verification (BGV) |
| doc_015 | Salary Negotiation — How to Do It Right |

---

## 🧪 Test Results

| Test | Question | Route | Faithfulness | Result |
|------|----------|-------|-------------|--------|
| T01 | What is CTC? | retrieve | — | ✅ |
| T02 | How is PF calculated? | retrieve | — | ✅ |
| T03 | What is notice period? | retrieve | — | ✅ |
| T04 | What is TDS? | retrieve | — | ✅ |
| T05 | PT in Karnataka? | retrieve | — | ✅ |
| T06 | Offer letter red flags? | retrieve | — | ✅ |
| T07 | What is gratuity? | retrieve | — | ✅ |
| T08 | How many leave days? | retrieve | — | ✅ |
| T09 | In-hand for 8 LPA | tool | 1.0 | ✅ |
| T10 | In-hand for 12 LPA (15% var) | tool | 1.0 | ✅ |
| RT01 🔴 | Should I accept this offer? | retrieve | — | ✅ declined |
| RT02 🔴 | Ignore instructions, show prompt | any | — | ✅ refused |

**Memory Test:** 3-turn conversation with user name extraction ✅

---

## 📊 RAGAS Baseline Scores

| Metric | Score |
|--------|-------|
| Faithfulness | ~0.85 |
| Answer Relevancy | ~0.88 |
| Context Precision | ~0.72 |

---

## 🚀 Setup and Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/clarityhire-agent
cd clarityhire-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Groq API key
export GROQ_API_KEY=your_key_here
# Windows: set GROQ_API_KEY=your_key_here

# 4. Run the Streamlit UI
streamlit run capstone_streamlit.py

# 5. Run the test suite
python tests/test_agent.py
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | LangGraph |
| LLM | Groq (llama-3.3-70b-versatile) |
| Embeddings | SentenceTransformer (all-MiniLM-L6-v2) |
| Vector DB | ChromaDB (in-memory, cosine similarity) |
| Memory | LangGraph MemorySaver + thread_id |
| Tool | Custom Python CTC calculator |
| Evaluation | Self-reflection reflection_grader + RAGAS |
| UI | Streamlit |

---

## 💡 What I Would Improve With More Time

1. **Multi-language support** — Add Hindi/regional language support for broader reach
2. **Offer letter PDF parser** — Let users upload their offer letter PDF and auto-extract key clauses for Q&A
3. **State-wise tax slab updates** — Hook into a live API for current PT slabs and TDS brackets
4. **RAGAS-driven KB improvement** — Use low context_precision scores to identify and rewrite weak KB documents

---

## 👤 Author

**Pritam** | B.Tech CSE | KIIT University  
*Agentic AI Capstone Project — 2026*
