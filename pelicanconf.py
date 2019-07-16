#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'miralin'
SITENAME = '...'
SITETITLE = '...'
SITESUBTITLE = 'There is no spoon'

SITEURL = ''

RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

THEME = 'themes/Flex'

STATIC_PATHS = ['images',
                'extra/robots.txt',
                ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CV', 'https://stavropol.hh.ru/resume/1ec8742fff02010ac20039ed1f427330524f71'),
         ('Codewars', 'https://www.codewars.com/users/MiraliN'),
         ('CheckiO', 'https://py.checkio.org/user/miralin'),
         ('Codesignal', 'https://app.codesignal.com/profile/miralin'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/MaxNorba'),
          ('linkedin', 'https://www.linkedin.com/in/miralin'),
          ('github', 'https://github.com/miralin'),
          ('bitbucket', 'https://bitbucket.org/Miralin'),
          )

DEFAULT_PAGINATION = 10

GITHUB_URL = 'https://github.com/miralin'
GITHUB_USER = 'miralin'

COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = 2019
