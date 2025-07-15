.PHONY: help clean clean-test clean-pyc clean-build lint format test watch cover build docs
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print(f"{target:20} {help}")
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr site/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -f cov.xml
	rm -fr .pytest_cache
	rm -f .testmondata
	rm -fr .hypothesis
	rm -fr .ruff_cache

lint: ## check style using ruff
	uv run ruff check src tests --fix

format: ## formatting check using ruff
	uv run ruff format src tests

test: ## run tests quickly with default Python
	uv run pytest tests

watch: ## continuously run unit tests on changed code
	uv run ptw .

cover: ## run tests quickly with default Python and check coverage
	uv run pytest --cov src --cov-report term --cov-report html
	open htmlcov/index.html

build: clean ## build package
	uv build

docs: ## Rebuild docs on changes, with live-reload in the browser
	uv run sphinx-autobuild docs docs/_build/html --open-browser
