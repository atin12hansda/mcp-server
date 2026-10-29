# Agent guide — MCP + LangGraph RAG

This repo is a greenfield FastMCP server that will host a LangGraph RAG pipeline over Streamable HTTP for remote Cursor clients.

## Layout

| Path | Role |
|------|------|
| `apps/mcp_server` | FastMCP HTTP adapter (`/mcp`, `/health`, MCP tools) |
| `packages/rag_core` | LangGraph RAG core (Phase 0: retrieve → generate stubs) |
| `data/kb/` | Seed markdown articles (not ingested in Phase 0) |
| `docs/PHASES.md` | Phases 0–4 scope and exit checks |
| `docs/cursor-mcp.md` | Connect Cursor to this server |

## Commands

```bash
make sync      # uv sync
make up        # docker compose up -d --build
make health    # curl GET /health
make logs      # follow container logs
make down      # stop stack
```

Local (no Docker): `make run-local` → listens on `0.0.0.0:8743`.

## Phase 0 constraints

- Stubs only: no real embeddings, LLM calls, triage routing, web UI, or auth.
- Postgres/pgvector runs in Compose for later phases; the app does not query it yet.
- Prefer changing `rag_core` for graph behavior and `mcp_server` for transport/tools.

## Approval workflow

Cursor proposes; humans approve plans and verify exit checks in `docs/PHASES.md` before advancing phases.
