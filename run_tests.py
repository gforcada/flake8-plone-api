# -*- coding: utf-8 -*-
from flake8_plone_api import CodingChecker

import unittest


class TestFlake8PloneAPI(unittest.TestCase):

    def test_get_replacement(self):
        checker = CodingChecker(None, 'test_file.py')
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 22)
        self.assertTrue(ret[0][2].startswith('P001 found '))


if __name__ == '__main__':
    unittest.main()
