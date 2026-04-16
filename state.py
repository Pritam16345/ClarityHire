"""
state.py — ClarityContextState TypedDict
Designed BEFORE all node functions (mandatory per rubric).
Every field a node writes must be declared here.
"""

from typing import TypedDict, List, Optional


class ClarityContextState(TypedDict):
    # Core RAG fields
    question: str
    messages: List[dict]           # Sliding window conversation history
    route: str                     # "retrieve" | "tool" | "memory_only"
    retrieved: str                 # Formatted retrieved context string
    sources: List[str]             # Source topic names from retrieval
    tool_result: str               # Output from calculator or other tools
    answer: str                    # Final answer from llm_generator
    faithfulness: float            # Eval score 0.0 – 1.0
    eval_retries: int              # Number of eval retries so far

    # Domain-specific fields
    user_name: str                 # Extracted from "my name is X"
    salary_inputs: dict            # Stores parsed salary inputs for tool
    query_category: str            # e.g. "salary" | "legal" | "negotiation" | "general"
    follow_up_suggestions: List[str]  # Proactive follow-up questions shown in UI
