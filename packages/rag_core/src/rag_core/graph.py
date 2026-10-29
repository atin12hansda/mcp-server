"""Stub LangGraph RAG pipeline: retrieve → generate.

Phase 0: no embeddings, no LLM calls. Nodes return deterministic stubs.
"""

from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class RagState(TypedDict):
    question: str
    documents: list[str]
    answer: str


def retrieve(state: RagState) -> dict[str, list[str]]:
    """Stub retrieve: pretend to fetch KB snippets for the question."""
    question = state["question"].strip() or "(empty question)"
    return {
        "documents": [
            f"[stub] No corpus ingested yet. Would search KB for: {question}",
        ]
    }


def generate(state: RagState) -> dict[str, str]:
    """Stub generate: format a placeholder answer from retrieved docs."""
    docs = state.get("documents") or []
    context = "\n".join(docs) if docs else "(no documents)"
    question = state.get("question", "")
    return {
        "answer": (
            "Phase 0 stub answer (no LLM).\n"
            f"Question: {question}\n"
            f"Context:\n{context}"
        )
    }


def build_graph():
    """Compile the retrieve → generate StateGraph."""
    graph = StateGraph(RagState)
    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)
    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)
    return graph.compile()


_GRAPH = None


def ask(question: str) -> dict[str, object]:
    """Run the stub RAG graph and return answer + documents."""
    global _GRAPH
    if _GRAPH is None:
        _GRAPH = build_graph()
    result = _GRAPH.invoke({"question": question, "documents": [], "answer": ""})
    return {
        "answer": result["answer"],
        "documents": result["documents"],
        "phase": 0,
        "stub": True,
    }
