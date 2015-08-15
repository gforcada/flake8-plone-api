# -*- coding: utf-8 -*-
__version__ = '1.1.0'


class CodingChecker(object):
    name = 'flake8_plone_api'
    version = __version__

    def __init__(self, tree, filename):
        self.filename = filename
