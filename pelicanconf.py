#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'librosa development team'
SITENAME = 'librosa blog'
SITEURL = 'https://librosa.org/blog'
SITESUBTITLE = '<code> import <span style="color: pink">librosa</span> </code>'
SITELOGO = '/images/librosa_logo.png'

PATH = 'content'
DEFAULT_CATEGORY = 'blog'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('home', 'https://librosa.org/'),
         ('documentation', 'https://librosa.org/librosa'),
         ('forum', 'https://groups.google.com/forum/#!forum/librosa'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

SOCIAL = (
    ('github', 'https://github.com/librosa/librosa'),
    ('rss', '/blog/feeds/all.atom.xml'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
]
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
IPYNB_NB_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.ipynb'

DEFAULT_PAGINATION = 10

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

THEME = 'themes/Flex'

COPYRIGHT_YEAR = '2019'
