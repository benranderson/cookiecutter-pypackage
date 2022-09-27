# Cookiecutter PyPackage

Cookiecutter template for a Python package.

## Features

- Command line interface using [Click](https://click.palletsprojects.com/en/8.1.x/)
- Testing setup with [pytest](https://docs.pytest.org/en/stable/)
- Test against multiple Python versions with [nox](https://nox.thea.codes/en/stable/)
- Continuous Integration using [azure-pipelines](https://azure.microsoft.com/en-gb/services/devops/pipelines/)
- Auto-release to an [Azure Artifacts Feed](https://azure.microsoft.com/en-us/services/devops/artifacts/) when you push a new tag
- Documentation using [Sphinx](https://www.sphinx-doc.org/en/master/) with [PyData Sphinx](https://pydata-sphinx-theme.readthedocs.io/en/stable/) theme
- [Pre-commit](https://pre-commit.com) hooks
- Makefile to automate setup, compilation, testing etc.

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
