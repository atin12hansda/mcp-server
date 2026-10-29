# Phase 0 MCP server image (FastMCP + stub rag_core)
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    MCP_HOST=0.0.0.0 \
    MCP_PORT=8743 \
    MCP_PATH=/mcp

COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock README.md ./
COPY apps/mcp_server/pyproject.toml apps/mcp_server/pyproject.toml
COPY packages/rag_core/pyproject.toml packages/rag_core/pyproject.toml
COPY apps/mcp_server/src apps/mcp_server/src
COPY packages/rag_core/src packages/rag_core/src
COPY data/kb data/kb

RUN uv sync --frozen --no-dev

EXPOSE 8743

# Call the venv entrypoint directly so startup does not rebuild workspace packages.
CMD ["/app/.venv/bin/mcp-server"]
