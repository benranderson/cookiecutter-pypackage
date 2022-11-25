# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Imports -----------------------------------------------------------------

import {{cookiecutter.project_slug}}

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{cookiecutter.project_slug}}"
copyright = "2022, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"

# The full version, including alpha/beta/rc tags
release = {{cookiecutter.project_slug}}.__version__
version = {{cookiecutter.project_slug}}.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_copybutton", "sphinx_click"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# Configure project logo
html_logo = "_static/logo.svg"

# Configure icon links
html_theme_options = {
    "icon_links": [
        {
            "name": "Git",
            "url": "{{ cookiecutter.repo_url }}",
            "icon": "fab fa-git-alt",
        }
    ]
}

# -- MyST Parser configuration -----------------------------------------------

# auto-generate header anchors
myst_heading_anchors = 3

myst_enable_extensions = ["colon_fence", "dollarmath"]
