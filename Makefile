IMAGE_NAME := selenium-tests

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it $(IMAGE_NAME)

run_decisionlab:
	docker run --rm -it --entrypoint venv/bin/python3 $(IMAGE_NAME) scrape_with_decisionlab.py

clean:
	docker rmi -f $(IMAGE_NAME)

all: build run clean

.PHONY: build run clean all
