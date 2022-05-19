"""Top-level package for {{ cookiecutter.project_name }}."""

import logging

__version__ = "{{ cookiecutter.version }}"
__title__ = "{{ cookiecutter.project_slug }}"
__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
__url__ = "{{ cookiecutter.repo_url }}"

logger = logging.getLogger()
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
