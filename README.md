# Cookiecutter PyPackage

Cookiecutter template for a Python package.

## Features

- Command line interface using [Click](https://click.palletsprojects.com/en/8.1.x/) and [rich-click](https://github.com/ewels/rich-click) for nice formatting
- Testing setup with [pytest](https://docs.pytest.org/en/stable/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov)
- Test against multiple Python versions with [nox](https://nox.thea.codes/en/stable/)
- Continuous Integration using [azure-pipelines](https://azure.microsoft.com/en-gb/services/devops/pipelines/)
- Auto-release to an [Azure Artifacts Feed](https://azure.microsoft.com/en-us/services/devops/artifacts/) when you push a new tag
- Documentation via [Sphinx](https://www.sphinx-doc.org/en/master/) using the [PyData Sphinx](https://pydata-sphinx-theme.readthedocs.io/en/stable/) theme and CLI docs auto-generated using [sphinx-click](https://github.com/click-contrib/sphinx-click)
- Linting using [Ruff](https://beta.ruff.rs/docs/)
- Code formatting using [Black](https://black.readthedocs.io/en/stable/)
- [Pre-commit](https://pre-commit.com) hooks
- `Makefile` (for macOS/Linux) and `make.bat` (for Windows) to automate setup, compilation, testing etc.

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
