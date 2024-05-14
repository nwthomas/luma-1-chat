build:
	docker-compose -f docker-compose.build.yml build

embed:
	python3 -m src.rag

install:
	pip install .

run:
	python3 main.py

run-docker:
	docker-compose up