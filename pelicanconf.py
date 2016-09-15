#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hendrik Schawe'
SITENAME = 'möchtegerngeek'
SITEURL = ''

TYPOGRIFY = True

THEME = 'themes/pelican-simplegrey'

PLUGIN_PATHS = ['plugins']
PLUGINS = ["render_math"]
MATH_JAX = {"source": "'//blog.schawe.me/mathjax/MathJax.js'"}

STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ich', 'https://hendrik.schawe.me'),)

# Social widget
SOCIAL = (('github', 'http://github.com/surt91'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
