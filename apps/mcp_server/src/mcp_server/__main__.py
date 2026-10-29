"""CLI entrypoint: python -m mcp_server"""

from mcp_server.app import run


def main() -> None:
    run()


if __name__ == "__main__":
    main()
