#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hendrik Schawe'
SITENAME = 'möchtegerngeek'
SITEURL = ''

TYPOGRIFY = True

DEFAULT_LANG = 'de'

DATE_FORMATS = {
    'de': '%d.%m.%Y',
}

DEFAULT_METADATA = {
    'status': 'draft',
}

#THEME = 'themes/pelican-simplegrey'
THEME = 'themes/pelican-elegant'

PLUGIN_PATHS = ['plugins']
PLUGINS = ["render_math", 
           "better_code_samples", 
           "tipue_search",
           "neighbors",
           "sitemap"
]
MATH_JAX = {"source": "'//blog.schawe.me/mathjax/MathJax.js'"}

READERS = {"html": None}
STATIC_PATHS = ['extra/favicon.ico', 
                'extra/jquery.min.js',
                'extra/bootstrap.min.js',
                'extra/bootstrap-combined.min.css',
                'theme/images', 
                'img',
                'vid',
                'js',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.ico': {'path': 'theme/images/favicon.ico'},
    'extra/jquery.min.js': {'path': 'jquery.min.js'},
    'extra/bootstrap.min.js': {'path': 'bootstrap.min.js'},
    'extra/bootstrap-combined.min.css': {'path': 'bootstrap-combined.min.css'},
    'extra/glyphicons-halflings-regular.woff2': {'path': 'glyphicons-halflings-regular.woff2'},
}

# Elegant theme
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
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
LINKS = (('Ich', 'https://hendrik.schawe.me'),
         ('Source','https://github.com/surt91/blog'),)

# Social widget
SOCIAL = (('github', 'https://github.com/surt91'),
          ('twitter', 'https://twitter.com/surt91'),
          ('youtube', 'https://www.youtube.com/surt91'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
