"""Top-level package for {{ cookiecutter.project_name }}."""

import logging
from importlib.metadata import version

__version__ = version(__package__)

logger = logging.getLogger(__package__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
