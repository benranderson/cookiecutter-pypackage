.PHONY: help clean clean-test clean-pyc clean-build lint test test-all build
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
	rm -fr .nox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -f cov.xml
	rm -fr .pytest_cache
	rm -f .testmondata
	rm -fr .hypothesis

lint: ## check style with flake8
	flake8 src tests noxfile.py

test: ## run tests quickly with default Python and check coverage
	pytest --cov src --cov-report term --cov-report html
	open htmlcov/index.html

test-all: ## run tests on every Python version with nox
	nox

safe: ## check for security vulnerabilities
	safety check --file=requirements.txt --full-report

build: clean ## build package
	python setup.py sdist bdist_wheel
