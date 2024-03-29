# {{ cookiecutter.project_name }} documentation

{{ cookiecutter.project_short_description }}

[![Build Status](https://dev.azure.com/technipfmc-dev/{{ cookiecutter.azure_project }}/_apis/build/status%{{ cookiecutter.project_slug }}%{{ cookiecutter.project_slug }}%20CI?branchName=master)](https://dev.azure.com/technipfmc-dev/{{ cookiecutter.azure_project }}/_build/latest?definitionId=242&branchName=master)
[![Python versions](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11-blue.svg)](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

---

**Source Code:** [{{ cookiecutter.repo_url }}]({{ cookiecutter.repo_url }})

**Version:** {{ cookiecutter.version }}

---

## Installation

```shell
pip install {{ cookiecutter.project_slug }}
```

```{toctree}
:hidden:
Command Reference <commands>
Release Notes <release-notes>
```
