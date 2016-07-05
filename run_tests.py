# -*- coding: utf-8 -*-
from flake8_plone_api import PloneAPIChecker
from tempfile import mkdtemp

import os
import unittest


class TestFlake8PloneAPI(unittest.TestCase):

    def _given_a_file_in_test_dir(self, contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_no_error_on_imports(self):
        file_path = self._given_a_file_in_test_dir(
            'from somewhere import getToolByName'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_get_replacement_end_of_line(self):
        file_path = self._given_a_file_in_test_dir(
            'from somewhere import getToolByName\n'
            '\n'
            'getToolByName(\n'
            '    3\n'
            ')\n'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 3)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('P001 found '))

    def test_get_replacement_nearly_end_of_line(self):
        file_path = self._given_a_file_in_test_dir(
            'from somewhere import getToolByName('
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 22)
        self.assertTrue(ret[0][2].startswith('P001 found '))

    def test_get_replacement_within_the_line(self):
        file_path = self._given_a_file_in_test_dir(
            'from plone import api\ntool = getToolByName(text)'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 7)
        self.assertTrue(ret[0][2].startswith('P001 found '))

    def test_get_multiple_replacement_options(self):
        file_path = self._given_a_file_in_test_dir(
            'from plone import checkPermission\n'
            '\n'
            'checkPermission(3)\n'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 3)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('P001 found '))
        self.assertNotEqual(ret[0][2].find(' or '), -1)

    def test_no_replacement_for_regular_code(self):
        file_path = self._given_a_file_in_test_dir(
            'from plone import api'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_replacement_is_substring_of_another_import(self):
        """One replacement is getSite -> portal.get but getSiteManager exists
        and gives a false positive.
        """
        file_path = self._given_a_file_in_test_dir(
            'from somewhere import getSiteManager'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_catalog_does_not_find_too_much(self):
        file_path = self._given_a_file_in_test_dir(
            'self.query_catalog(**query)[:limit]'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_version(self):
        file_path = self._given_a_file_in_test_dir(
            'from plone import searchResults\n'
            '\n'
            'searchResults(3)\n'
        )
        checker = PloneAPIChecker(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 3)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('P001 found '))
        self.assertIn('1.3.3', ret[0][2])


if __name__ == '__main__':
    unittest.main()
