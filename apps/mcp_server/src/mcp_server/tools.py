"""MCP tool registrations (Phase 0 stubs)."""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from rag_core import ask


def register_tools(mcp: FastMCP) -> None:
    """Attach Phase 0 stub tools to the FastMCP server."""

    @mcp.tool
    def kb_stats() -> dict[str, Any]:
        """Return stub knowledge-base statistics (not ingested yet)."""
        return {
            "status": "not_ingested",
            "documents": 0,
            "chunks": 0,
            "embedding_model": None,
            "note": "Phase 0 stub — seed files live in data/kb/ but are not ingested.",
        }

    @mcp.tool
    def search_kb(query: str, limit: int = 5) -> dict[str, Any]:
        """Stub KB search. Returns empty hits until ingestion exists."""
        return {
            "query": query,
            "limit": limit,
            "hits": [],
            "stub": True,
            "note": "Phase 0 stub — no vector search yet.",
        }

    @mcp.tool
    def ask_docs(question: str) -> dict[str, Any]:
        """Ask a question via the stub LangGraph RAG pipeline."""
        return ask(question)

    @mcp.tool
    def triage_ticket(
        subject: str,
        body: str = "",
        priority: str | None = None,
    ) -> dict[str, Any]:
        """Stub ticket triage — no real routing in Phase 0."""
        return {
            "subject": subject,
            "body": body,
            "priority_in": priority,
            "suggested_queue": "unassigned",
            "suggested_priority": priority or "normal",
            "confidence": 0.0,
            "stub": True,
            "note": "Phase 0 stub — real triage routing is out of scope.",
        }
