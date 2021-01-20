# Cookiecutter PyPackage

Cookiecutter template for a Python package.

## Features

- Command line interface using Typer
- Testing setup with pytest
- Test multiple Pythons with nox
- Continuous Integration using azure-pipelines
- Auto-release to an Azure Artifacts Feed when you push a new tag
- Documentation using MkDocs
- Pre-commit hooks
- Makefile to clean up files

Cookiecutter: [https://github.com/cookiecutter/cookiecutter](https://github.com/cookiecutter/cookiecutter)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```shell
pip install -U cookiecutter
```

Generate a Python package project:

```shell
cookiecutter https://github.com/benranderson/cookiecutter-pypackage
```
