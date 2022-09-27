"""{{ cookiecutter.project_name }} setup script."""

import re
from pathlib import Path

from setuptools import find_packages, setup

META_PATH = Path("src/{{ cookiecutter.project_slug }}/__init__.py")


def find_meta(meta):
    """Extract __*meta*__ from META_FILE."""
    with open(META_PATH) as f:
        meta_match = re.search(f"^__{meta}__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError(f"Unable to find __{meta}__ string.")


def get_file_contents(filename, splitlines=False):
    with Path(filename).open(mode="r") as fh:
        if splitlines:
            return fh.read().splitlines()
        return fh.read()


setup(
    name=find_meta("title"),
    description="{{ cookiecutter.project_short_description }}",
    long_description=get_file_contents("README.md"),
    version=find_meta("version"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    maintainer=find_meta("author"),
    maintainer_email=find_meta("email"),
    url=find_meta("url"),
    install_requires=get_file_contents("requirements.txt", splitlines=True),
    extras_require={"dev": get_file_contents("requirements-dev.txt", splitlines=True)},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    entry_points={"console_scripts": ["{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.__main__:app"]},
)
