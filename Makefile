.PHONY: app

APP_PATH := src/main.py

init:
	./resources/scripts/init.sh

app:
	PYTHONPATH=./src/ uv run $(APP_PATH)