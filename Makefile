.PHONY: install check run up down

install:
	python -m pip install -r requirements-dev.txt

check:
	ruff check .
	pytest

run:
	python -m app

up:
	docker compose up --build

down:
	docker compose down
