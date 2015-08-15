# -*- coding: utf-8 -*-
from mapping import get_mapping


__version__ = '0.1'

MAPPING = get_mapping()


class CodingChecker(object):
    name = 'flake8_plone_api'
    version = __version__
    message = 'P001 found "{0}" consider replacing it with: {1}'

    def __init__(self, tree, filename):
        self.filename = filename

    def run(self):
        with open(self.filename) as f:
            lines = f.readlines()

            for lineno, line in enumerate(lines, start=1):
                for old_approach in MAPPING:
                    found = line.find(old_approach)
                    if found != -1:
                        msg = self.message.format(
                            old_approach,
                            ' or '.join(MAPPING[old_approach])
                        )
                        yield lineno, found, msg, type(self)
