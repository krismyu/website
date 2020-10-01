#!/usr/bin/env python
# -*- coding: utf-8 --*-- #
from __future__ import unicode_literals

AUTHOR = u'Kristine M. Yu'
SITESUBTITLE = u'Linguist at UMass Amherst'
SITENAME = u'Kristine M. Yu'
SITEURL = ''


DEFAULT_DATE_FORMAT = '%Y %B %d'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'


# Formatting for urls, archives

ARTICLE_URL = "blog/posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/posts/{date:%Y}/{date:%m}/{slug}/index.html"
YEAR_ARCHIVE_SAVE_AS = 'blog/posts/{date:%Y}/index.html'

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

ARCHIVES_SAVE_AS = "archives.html"

# display items
#LOGO_URL = 'https://dl.dropboxusercontent.com/u/7030113/www/art-noveau-ornament.png'
MENUITEMS = [('output', '/output'),             
             ('teaching', '/teaching'),
             ('resources', '/resources'),
             ('vita', '/vita'),
             ('blog', '/'),
             ('archives', '/archives.html')]
DISPLAY_PAGES_ON_MENU = False
NEWEST_FIRST_ARCHIVES = False


#Github include settings
GITHUB_USER = 'krismyu'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Search box
SEARCH_BOX = True

FOOTER_MESSAGE = u'This work is licensed under the <a href="http://creativecommons.org/licenses/by-sa/3.0/" rel="license">CC BY-SA</a>.'
TWITTER_USERNAME = u'kfr_2'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('UMass Linguistics', 'http://www.umass.edu/linguist'),
#          ('Python.org', 'http://python.org/'),
#          ('UMass Phonetics Lab', 'people.umass.edu/phonetic'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

LOCALE = 'en_US'

# Set theme
THEME = '../themes/pelican-octopress-theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Set static paths
STATIC_PATHS = ["blog/img", "blog/data", "blog/videos", "pages/home", "pages/output", "pages/resources", "pages/teaching", "pages/vita", "pages/masspros"]

# Plugins
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['latex', 'neighbors', 'summary']

# Only use LaTeX for selected articles

LATEX = 'article'

# Commenting, site statistics
DISQUS_SITENAME = 'krisyu'

PIWIK_URL = 'www.piwik.krisyu.org'
#PIWIK_SSL_URL = ''
PIWIK_SITE_ID = '2'
