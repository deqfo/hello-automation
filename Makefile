.PHONY: run test lint format

run:
	uv run python main.py

test:
	uv run ruff check
	uv run ruff format
	uv run mypy main.py