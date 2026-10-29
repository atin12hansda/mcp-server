"""FastMCP application: Streamable HTTP on /mcp plus GET /health."""

from __future__ import annotations

import os

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

from mcp_server.tools import register_tools

HOST = os.getenv("MCP_HOST", "0.0.0.0")
PORT = int(os.getenv("MCP_PORT", "8743"))
PATH = os.getenv("MCP_PATH", "/mcp")


def create_mcp() -> FastMCP:
    mcp = FastMCP(
        name="mcp-server",
        instructions=(
            "Phase 0 FastMCP server hosting a stub LangGraph RAG pipeline. "
            "Tools: kb_stats, search_kb, ask_docs, triage_ticket."
        ),
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health(_request: Request) -> JSONResponse:
        return JSONResponse(
            {
                "status": "ok",
                "service": "mcp-server",
                "phase": 0,
                "mcp_path": PATH,
            }
        )

    register_tools(mcp)
    return mcp


mcp = create_mcp()


def run() -> None:
    """Serve Streamable HTTP for remote Cursor clients."""
    mcp.run(
        transport="http",
        host=HOST,
        port=PORT,
        path=PATH,
    )
