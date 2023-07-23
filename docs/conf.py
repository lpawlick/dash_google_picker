# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_material
import sphinx_js
import os
import sys

# Add the path to your module folder
sys.path.insert(0, os.path.abspath('..'))
js_source_path = '../src/lib/components/'

project = 'Dash Google Picker documentation'
copyright = '2023, lpawlick'
author = 'lpawlick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_js", "sphinx.ext.autodoc"]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
html_title = "Dash Google Picker"
html_sidebars = {
    '**': [ 'about.html',
            'postcard.html', 'navigation.html',
            'recentposts.html', 'tagcloud.html',
            'categories.html',  'archives.html',
            'searchbox.html', #'logo-text.html',
            'globaltoc.html', #'localtoc.html'
            ],
    }
html_theme_options = {
    #'touch_icon' : '',
    'base_url' : '/',
    'globaltoc_depth' : -1,
    'theme_color' : '5F021F',
    'color_primary' : 'red',
    'color_accent' : 'red',
    #'html_minify' : True,
    'css_minify' : True,
    #'logo_icon' : '',
}