# Cookiecutter PyPackage

[Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for a Python package.

## Features

- Command line interface using [Click](https://click.palletsprojects.com/en/8.1.x/) and [rich-click](https://github.com/ewels/rich-click) for nice formatting
- Testing setup with [pytest](https://docs.pytest.org/en/stable/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov)
- Continuous Integration using [azure-pipelines](https://azure.microsoft.com/en-gb/services/devops/pipelines/)
- Auto-release to an [Azure Artifacts Feed](https://azure.microsoft.com/en-us/services/devops/artifacts/) when you push a new tag
- Documentation via [Sphinx](https://www.sphinx-doc.org/en/master/) using the [PyData Sphinx](https://pydata-sphinx-theme.readthedocs.io/en/stable/) theme and CLI docs auto-generated using [sphinx-click](https://github.com/click-contrib/sphinx-click)
- Formatting and linting using [Ruff](https://beta.ruff.rs/docs/)
- [Pre-commit](https://pre-commit.com) hooks
- `Makefile` (for macOS/Linux) and `make.bat` (for Windows) to automate setup, compilation, testing etc.

## Quickstart

Install the latest version of Cookiecutter:

```shell
uv tool install cookiecutter
```

Generate a personal access token for Azure DevOps with `Code (Read)` and `Packaging (Read)` scopes.

Generate a Python package project, replacing `<PAT>` with your personal access token:

```shell
cookiecutter https://<PAT>@dev.azure.com/technipfmc-dev/SubseaDesign/_git/cookiecutter-pypackage
```

Navigate to the newly created project directory.

Set your environment variables for authentication in a new `env.bat` file and run it:

```env
set UV_INDEX_ADO_USERNAME=dummy
set UV_INDEX_ADO_PASSWORD=<PAT>
```

Run the following command to create the virtual environment and install the project dependencies:

```shell
uv sync
```
