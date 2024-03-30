import datetime

AUTHOR = 'MiraliN'
SITENAME = '...'
SITETITLE = '...'
SITESUBTITLE = 'There is no spoon'
SITEURL = ''

RELATIVE_URLS = False

GITHUB_URL = 'https://github.com/miralin'
GITHUB_USER = 'miralin'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
I18N_TEMPLATES_LANG = "ru"
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
         ('Exercism', 'https://exercism.io/profiles/miralin')
         )

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/miralin'),
          ('github', 'https://github.com/miralin'),
          ('bitbucket', 'https://bitbucket.org/Miralin'),
          ('gitlab', 'https://gitlab.com/Miralin'),
          ('lastfm', 'https://www.last.fm/ru/user/Fobinho'),
          ('reddit', 'https://www.reddit.com/user/MiraliN'),
          )

DEFAULT_PAGINATION = 10

COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.date.today().year
