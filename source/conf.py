# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath("."))
project = 'Hydrodata'
copyright = '2023, Princeton University, University of Arizona'
author = 'Bill Hasling, Amy Johnson, Amy Defnet, Reed Maxwell, Laura Condon'
release = '1.0.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']