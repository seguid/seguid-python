# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'seguid'
copyright = '2023, bjorn'
author = 'bjorn'

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
	"biopython": ("https://biopython.org/docs/latest/api/", None),
	"python": ("http://docs.python.org/3.8", None),
}

autodoc_member_order = 'bysource'
autodoc_preserve_defaults = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
