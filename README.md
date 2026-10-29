# mcp-server

Greenfield **FastMCP** server hosting a **LangGraph** RAG pipeline (Phase 0: stubs) over **Streamable HTTP**, with Docker Compose (`mcp` + **pgvector** Postgres).

## Quick start

```bash
cp .env.example .env
make up
make health
```

- MCP: `http://127.0.0.1:8743/mcp`
- Health: `http://127.0.0.1:8743/health`

Connect Cursor: see [docs/cursor-mcp.md](docs/cursor-mcp.md). Phases: [docs/PHASES.md](docs/PHASES.md). Agent notes: [AGENTS.md](AGENTS.md).

## Layout

```text
apps/mcp_server/     FastMCP adapter + tools
packages/rag_core/   LangGraph retrieve → generate
data/kb/             Seed markdown (not ingested yet)
docs/                Phases + Cursor connect guide
```

## Make targets

| Target | Action |
|--------|--------|
| `make sync` | `uv sync` |
| `make up` | Build & start Compose |
| `make health` | `GET /health` |
| `make logs` | Follow logs |
| `make down` | Stop stack |
| `make run-local` | Run without Docker |
