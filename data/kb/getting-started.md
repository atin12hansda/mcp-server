# Getting started with the knowledge base

This is a **seed article** for Phase 0. It is not ingested into pgvector yet.

## Purpose

The MCP server will eventually answer questions from documents in `data/kb/` using a LangGraph retrieve → generate pipeline.

## Phase 0 behavior

- Files in this folder are samples only.
- `search_kb` and `kb_stats` return stubs.
- `ask_docs` runs a stub graph without embeddings or LLM calls.

## Next

Phase 1 will chunk and embed this content into Postgres with pgvector.
