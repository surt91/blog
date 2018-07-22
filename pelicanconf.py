#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hendrik Schawe'
SITENAME = 'möchte&shy;gern&shy;geek'
# SITESUBTITLE = 'lorem ipsum dolor sit amet'
SITEURL = 'https://blog.schawe.me'

PINNED_POST = "randomFractals"

TYPOGRIFY = True

DATE_FORMATS = {
    'de': '%d.%m.%Y',
    'en': '%m/%d/%Y',
}

DEFAULT_METADATA = {
    'status': 'draft',
}

THEME = 'themes/purepelican'
from themes.purepelican.settings import *

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    "assets",
    "render_math",
    "tipue_search",
    "neighbors",
    "sitemap",
    "preload_thumbnail",
    "i18n_subsites",
]

DEFAULT_LANG = "de"
I18N_SUBSITES = {
    # 'de': {
    #     'SITE_DESCRIPTION': 'Dinge, die ich für hübsch, praktisch oder interessant halte.',
    # }
    'en': {
        'SITE_DESCRIPTION': 'Things I consider pretty, practical or interesting.',
    }
}
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

READERS = {"html": None}
STATIC_PATHS = [
    'extra/manifest.json',
    'extra/service-worker-registration.js',
    'extra/service-worker-registration.min.js',
    'extra/_headers',
    'extra/custom.css',
    'extra/favicon.ico',
    'extra/icons',
    'theme/images',
    'extra/googlee1eadb2ddedaa639.html',
    'img',
    'vid',
    'js',
]

EXTRA_PATH_METADATA = {
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/service-worker-registration.js': {'path': 'service-worker-registration.js'},
    'extra/service-worker-registration.min.js': {'path': 'service-worker-registration.min.js'},
    'extra/_headers': {'path': '_headers'},
    'extra/custom.css': {'path': 'custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googlee1eadb2ddedaa639.html': {'path': 'googlee1eadb2ddedaa639.html'},
}

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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# (linktext, link, [font awesome symbol])
SOCIAL = (
    ('Ich', 'https://hendrik.schawe.me', 'user'),
    ('GitHub', 'https://github.com/surt91'),
    ('Email', 'mailto:hendrik.schawe+blog@gmail.com', 'envelope'),
    ('Twitter', 'https://twitter.com/surt91'),
)

DEFAULT_PAGINATION = 3
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
