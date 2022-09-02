SHELL := /bin/bash

.PHONY: install lint test black isort format

install:
	pip install -e .[dev,test]

lint:
	flake8

test:
	py.test

black:
	black -v --check .

isort:
	isort --check-only pubsub_opentelemetry

format:
	black pubsub_opentelemetry
	black tests
	isort pubsub_opentelemetry
	isort tests
