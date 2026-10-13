# -*- coding: utf-8 -*-
#
# the sphinx configuration of the AlTar 2 tutorials

project = 'AlTar 2 tutorials'
copyright = '2013-present ParaSim Inc., 2010-present California Institute of Technology'
author = 'AlTar Development Team'
release = '2.0'

extensions = [
    'nbsphinx', # include jupyter notebooks
    'myst_parser', # markdown support
    'sphinx.ext.mathjax', # render math via JavaScript
]

master_doc = 'index'
exclude_patterns = ['_build', 'README.md', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints',
                    '**/results']
html_theme = 'sphinx_rtd_theme'

# the notebooks are stored with their outputs; refresh them with `python run.py --update`
nbsphinx_execute = 'never'

myst_enable_extensions = ["dollarmath", "amsmath"]
source_suffix = {
    '.md': 'markdown',
}
latex_engine = 'xelatex'

# end of file
