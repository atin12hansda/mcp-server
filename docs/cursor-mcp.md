# Connect Cursor to this MCP server

Phase 0 serves **Streamable HTTP** at:

```text
http://127.0.0.1:8743/mcp
```

## Prerequisites

1. Stack is up: `make up` (or `make run-local`).
2. Health works: `make health` → `"status": "ok"`.
3. If Cursor runs on another machine, forward port `8743` (SSH tunnel example below) so the client still uses `127.0.0.1`.

### SSH tunnel (remote Docker host)

```bash
ssh -L 8743:127.0.0.1:8743 user@your-server
```

## Cursor MCP config

Add a server entry in Cursor MCP settings (UI or `mcp.json`), for example:

```json
{
  "mcpServers": {
    "mcp-server": {
      "url": "http://127.0.0.1:8743/mcp"
    }
  }
}
```

Exact JSON keys can vary by Cursor version; choose the **HTTP / Streamable HTTP** transport (not stdio) and point it at `/mcp`.

## Verify

1. Reload MCP servers in Cursor.
2. Confirm tools appear: `kb_stats`, `search_kb`, `ask_docs`, `triage_ticket`.
3. Call `kb_stats` — expect a Phase 0 stub noting the KB is not ingested.
4. Call `ask_docs` with any question — expect stub retrieve→generate text.

## Notes

- No auth in Phase 0 — bind carefully; prefer localhost + tunnel.
- MCP path is configurable via `MCP_PATH` (default `/mcp`).
- Health is separate: `GET http://127.0.0.1:8743/health` (not under `/mcp`).
