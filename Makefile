SHELL := /bin/bash

.PHONY: install lint format release build

install:
	pip install -e .[dev,test]

lint:
	flake8

test:
	pytest

tox $(TOX_ENV):
	[ -z "$(TOX_ENV)" ] && tox || tox -e $(TOX_ENV)

build:
	python -m build

release: build
	twine upload dist/*

format:
	black pubsub_opentelemetry
	black tests
	isort pubsub_opentelemetry
	isort tests
