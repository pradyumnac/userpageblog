#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

CURRENTYEAR = date.today().year

AUTHOR = 'pradyumnac'
SITENAME = 'Pradyumna Chatterjee'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = [
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/LICENSE': {'path': 'LICENSE'},
}

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Utility: IndiaVIX Autoreport', 'https://pradyumnac.github.io/IndiaVIX/'),
         ('Story Series: Deep Space Man (A Story)', 'https://alternate-media.github.io/deep-space-man/'),
         ('Blog: Growth WHAT?', 'https://alternate-media.github.io/growth-what/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/pradyumnac'),
          ('Linkedin', 'https://www.linkedin.com/in/pradyumnac/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "D:/Projects/Blogs/Pelican/themes/octopress"