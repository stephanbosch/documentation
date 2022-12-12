# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys
import subprocess
sys.path.append(os.path.abspath('./_ext'))

# Increase recursion limit; needed for todo processing
sys.setrecursionlimit(10000)

from sphinx.environment import default_settings

# -- Project information -----------------------------------------------------

project = u'Dovecot'
copyright = u'Dovecot Authors'
author = u'Dovecot Authors'

version = os.getenv('GITHUB_SHA')
if not version:
    version = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode()
release = version

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx_removed_in',
    'dovecot_sphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_title = "Dovecot documentation"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'font_family': 'Roboto',
  'logo' : 'dovecot.gif',
#  'github_user': 'dovecot',
#  'github_repo': 'core',
  'github_banner': False,
  'extra_nav_links': {
    'Edit Documentation': 'https://github.com/dovecot/documentation/pulls/',
    'Repositories' : 'https://repo.dovecot.org/',
    'Download'     : 'https://dovecot.org/download.html',
  },
  'show_powered_by': True,
  'page_width': '92%',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static/']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'license.html',
    ]
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Dovecotdoc'

html_css_files = [
 'https://s3-us-west-2.amazonaws.com/colors-css/2.2.0/colors.min.css',
]


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Dovecot.tex', u'Dovecot Documentation',
     u'Dovecot Authors', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
#man_pages = [
#    ('man/dovecot', 'dovecot', u'Dovecot Documentation',
#     [author], 1)
#]

man_pages = []

for man_dir in os.listdir("."):
    if os.path.isdir(man_dir) == False:
        continue
    if (man_dir == "man" or man_dir.endswith("-man")) and tags.tags.get(man_dir):
        for man_page in os.listdir(man_dir):
            if man_page.endswith(".rst.in"):
                man_pages.append(("%s/%s" % (man_dir, man_page[0:-7]), man_page[0:-9], u'', [author], int(man_page[-8:-7])))

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('man/index', 'Dovecot', u'Dovecot Documentation',
     author, 'Dovecot', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

todo_include_todos = False

default_settings['rfc_base_url'] = "https://datatracker.ietf.org/doc/html/"
