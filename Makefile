DOCKER_TAG := fastsvelte
HOST := 0.0.0.0
PORT := 8080

dev:
	fastapi dev --host $(HOST) --port $(PORT) --reload server.py

run:
	fastapi run --host $(HOST) --port $(PORT) --reload server.py

build:
	cd web; make build
