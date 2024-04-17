# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'seguid'
copyright = '2024, Bjorn Johansson, Henrik Bengtsson, Louis Abraham'
author = 'Bjorn Johansson, Henrik Bengtsson, Louis Abraham'

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
			  'sphinx.ext.coverage',
			  'sphinx.ext.napoleon',
			  "sphinx.ext.doctest",
			  "sphinx.ext.viewcode",
			  "sphinx.ext.autosummary",
			  "numpydoc",
			  "sphinx.ext.intersphinx",]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
	"python": ("http://docs.python.org/3.8", None),
}

autodoc_member_order = 'bysource'
autodoc_preserve_defaults = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    'extra_nav_links': {
        "Home page": "https://www.seguid.org",
        "Source code": "https://github.com/seguid/seguid-python",
        "Issue Tracker": "https://github.com/seguid/seguid-python/issues"
    }
}
