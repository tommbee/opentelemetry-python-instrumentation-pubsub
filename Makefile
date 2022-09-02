SHELL := /bin/bash

.PHONY: install lint test format

install:
	pip install -e .[dev,test]

lint:
	flake8

test:
	pytest

format:
	black pubsub_opentelemetry
	black tests
	isort pubsub_opentelemetry
	isort tests
