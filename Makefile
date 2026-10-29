.PHONY: help sync up down build logs health restart ps shell

help: ## Show targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

sync: ## Install workspace deps with uv
	uv sync

up: ## Build and start Compose stack (mcp + pgvector)
	docker compose up -d --build

down: ## Stop Compose stack
	docker compose down

build: ## Build mcp image
	docker compose build

logs: ## Tail mcp + postgres logs
	docker compose logs -f mcp postgres

restart: ## Restart mcp service
	docker compose restart mcp

ps: ## Show Compose status
	docker compose ps

health: ## GET /health on local MCP port
	@curl -sf "http://127.0.0.1:$${MCP_PORT:-8743}/health" | python3 -m json.tool

shell: ## Shell into running mcp container
	docker compose exec mcp /bin/sh

run-local: ## Run MCP locally via uv (no Docker)
	uv run mcp-server
