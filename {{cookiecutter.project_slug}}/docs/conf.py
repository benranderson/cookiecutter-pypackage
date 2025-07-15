# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Imports -----------------------------------------------------------------
import time

import {{cookiecutter.project_slug}}

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{cookiecutter.project_slug}}"
copyright = f"{time.strftime('%Y')}, TechnipFMC"
author = "{{ cookiecutter.full_name }}"

# The full version, including alpha/beta/rc tags
release = {{cookiecutter.project_slug}}.__version__
version = {{cookiecutter.project_slug}}.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_copybutton", "sphinx_click", "sphinx.ext.autodoc"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Table and Figure config (only considered for LaTeX output)
numfig = True
numfig_format = {"figure": "Figure %s"}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
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
