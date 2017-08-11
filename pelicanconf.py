#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hendrik Schawe'
SITENAME = 'möchtegerngeek'
SITEURL = 'https://blog.schawe.me'

TYPOGRIFY = True

DEFAULT_LANG = 'de'

DATE_FORMATS = {
    'de': '%d.%m.%Y',
}

DEFAULT_METADATA = {
    'status': 'draft',
}

# THEME = 'themes/pelican-simplegrey'
THEME = 'themes/pelican-elegant'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    "render_math",
    "better_code_samples",
    "tipue_search",
    "neighbors",
    "sitemap"
]

READERS = {"html": None}
STATIC_PATHS = [
    'extra/custom.css',
    'extra/favicon.ico',
    'extra/jquery.min.js',
    'extra/bootstrap.min.js',
    'extra/bootstrap-combined.min.css',
    'extra/CNAME',
    'theme/images',
    'extra/googlee1eadb2ddedaa639.html',
    'img',
    'vid',
    'js',
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/css/custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googlee1eadb2ddedaa639.html': {'path': 'googlee1eadb2ddedaa639.html'},
    'extra/jquery.min.js': {'path': 'jquery.min.js'},
    'extra/bootstrap.min.js': {'path': 'bootstrap.min.js'},
    'extra/bootstrap-combined.min.css': {'path': 'bootstrap-combined.min.css'},
    'extra/glyphicons-halflings-regular.woff2': {'path': 'glyphicons-halflings-regular.woff2'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Elegant theme
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True
SITE_DESCRIPTION = 'Dinge, die ich für hübsch, praktisch oder interessant halte.'
FEATURED_IMAGE = 'https://blog.schawe.me/img/logo.png'

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
LINKS = (
    ('Ich', 'https://hendrik.schawe.me'),
    ('Source', 'https://github.com/surt91/blog'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/surt91'),
    ('Email', 'mailto:hendrik.schawe+blog@gmail.com'),
    ('Twitter', 'https://twitter.com/surt91'),
    ('YouTube', 'https://www.youtube.com/surt91'),
)

DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
