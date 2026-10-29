# Phases 0–4

## Phase 0 — Scaffold (current)

**Goal:** Runnable FastMCP HTTP server + stub LangGraph + Compose (mcp + pgvector).

| Deliverable | Status target |
|-------------|---------------|
| `apps/mcp_server` + `packages/rag_core` | Present |
| Streamable HTTP on `0.0.0.0:8743` path `/mcp` | Live |
| `GET /health` | 200 JSON |
| Stub graph retrieve → generate | Invoked by `ask_docs` |
| Tools: `kb_stats`, `search_kb`, `ask_docs`, `triage_ticket` | Registered (stubs OK) |
| Dockerfile, Compose, Makefile, `.env.example`, `.gitignore` | Present |
| `AGENTS.md`, this file, Cursor connect docs | Present |
| `data/kb/` seed markdown | Present, not ingested |

**Out of scope:** embeddings/LLM, real triage, web UI, auth.

### Exit checks

1. `docker compose up -d --build` succeeds; `postgres` healthy; `mcp` running.
2. `curl -sf http://127.0.0.1:8743/health` returns `"status":"ok"`.
3. MCP endpoint reachable at `http://127.0.0.1:8743/mcp` (Cursor can list tools).
4. Tools return stub payloads; `ask_docs` shows retrieve→generate stub text.
5. No code path calls an external LLM or embedding API.

---

## Phase 1 — Ingest + pgvector

**Goal:** Chunk/embed seed KB into Postgres (pgvector); `search_kb` / `kb_stats` become real.

### Exit checks

1. Ingest CLI/job loads `data/kb/` into pgvector.
2. `kb_stats` reports non-zero documents/chunks.
3. `search_kb` returns ranked hits for a known phrase from seed articles.
4. Embeddings use a configured model; secrets only via env.

---

## Phase 2 — Real RAG generate

**Goal:** Wire LLM into `generate`; `ask_docs` answers from retrieved context.

### Exit checks

1. `ask_docs` returns grounded answers citing retrieved chunks.
2. Missing-context questions degrade gracefully (no hallucinated KB claims required).
3. Token/model settings documented in `.env.example`.

---

## Phase 3 — Triage routing

**Goal:** `triage_ticket` classifies queue/priority using RAG + rules/LLM.

### Exit checks

1. Given sample tickets, suggested queue/priority are deterministic or evaluated against a fixture set.
2. Confidence and rationale fields returned.
3. Still no public web UI; MCP remains the interface.

---

## Phase 4 — Hardening

**Goal:** Auth, observability, and production readiness for remote Cursor.

### Exit checks

1. Auth on MCP (or network policy documented + implemented).
2. Structured logs/metrics; health distinguishes liveness vs dependency readiness.
3. Docs cover remote Cursor + tunnel/firewall; Compose (or deploy) is reproducible from clean clone.
