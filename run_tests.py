import os
import textwrap
from unittest import mock

from flake8_plone_api import PloneAPIChecker


def write_python_file(tmpdir, content):
    source = textwrap.dedent(content)
    file_path = os.path.join(str(tmpdir), 'test.py')
    with open(file_path, 'w') as python_file:
        python_file.write(source)
    return file_path


def check_code(source, tmpdir, expected_codes=None):
    """Check if the given source code generates the given flake8 errors

    If `expected_codes` is a string is converted to a list,
    if it is not given, then it is expected to **not** generate any error.
    """
    if isinstance(expected_codes, str):
        expected_codes = [expected_codes]
    elif expected_codes is None:
        expected_codes = []

    file_path = write_python_file(tmpdir, source)
    checker = PloneAPIChecker(None, file_path)
    return_values = list(checker.run())

    assert len(return_values) == len(expected_codes)
    for item, code in zip(return_values, expected_codes):
        assert item[2].startswith(f'{code} ')


def test_all_good(tmpdir):
    source = 'import os'
    check_code(source, tmpdir)


def test_error(tmpdir):
    source = 'createContentInContainer("foo")'
    check_code(source, tmpdir, 'P001')


def test_line(tmpdir):
    source = """
    a = 3
    createContentInContainer(a, "max")
    """
    file_path = write_python_file(tmpdir, source)
    checker = PloneAPIChecker(None, file_path)
    return_values = list(checker.run())

    assert return_values[0][0] == 3


def test_column(tmpdir):
    source = """
    class MyObject:
        def my_function(self):
            createContentInContainer(a, "max")
    """
    file_path = write_python_file(tmpdir, source)
    checker = PloneAPIChecker(None, file_path)
    return_values = list(checker.run())

    assert return_values[0][1] == 8


@mock.patch('flake8_plone_api.stdin_utils.stdin_get_value')
def test_stdin(stdin_get_value):
    source = """
    a = 3
    createContentInContainer(a, "max")
    """
    stdin_value = mock.Mock()
    stdin_value.splitlines.return_value = textwrap.dedent(source).split('\n')
    stdin_get_value.return_value = stdin_value

    checker = PloneAPIChecker(None, 'stdin')
    return_values = list(checker.run())
    assert len(return_values) == 1
