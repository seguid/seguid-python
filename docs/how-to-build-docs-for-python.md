### How to generate docs from docstrings with Sphinx

in terminal:

`micromamba install spinx numpydoc # or install with conda, mamba`

`pip install --editable . --no-deps # the project to be documented must be installed`



In the root of the project (location of setup.py or pyproject.toml)

    sphinx-quickstart docs

This should only be done once and generates the docs directory and some files, including the conf.py

Add this to conf.py:

    import os
    import sys
    sys.path.insert(0, os.path.abspath("../src"))

    extensions = ['sphinx.ext.autodoc',
                  'sphinx.ext.coverage',
                  'sphinx.ext.napoleon',
                  "sphinx.ext.doctest",
                  "sphinx.ext.viewcode",
                  "sphinx.ext.autosummary",
                  "numpydoc",
                  "sphinx.ext.intersphinx",]

    intersphinx_mapping = {
        "biopython": ("https://biopython.org/docs/latest/api/", None),
        "python": ("http://docs.python.org/3.8", None),
    }

    autodoc_member_order = 'bysource'
    autodoc_preserve_defaults = True

Then:

    sphinx-apidoc --force --no-toc --no-headings --output-dir docs .

This will generate several .rst files. For small projects, all content can be put in the
index.rst file:

        .. seguid documentation master file, created by
           sphinx-quickstart on Thu Oct 19 14:14:11 2023.
           You can adapt this file completely to your liking, but it should at least
           contain the root `toctree` directive.

        seguid module
        =============

        .. automodule:: seguid
           :members:
           :undoc-members:
           :show-inheritance:

Finally, to build or rebuild:

    sphinx-build . _build/html&&xdg-open _build/html/index.html
