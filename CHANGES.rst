.. -*- coding: utf-8 -*-

Changelog
=========

1.5.0 (2022-10-09)
------------------

- Pin dependencies. [gforcada]

- Test//QA with GitHub actions. [gforcada]

- Overhaul testing. [gforcada]

1.4 (2017-05-31)
----------------
- Fixed false positive "default_language" string match. (issue #17)
  [iham]

- Fix conflict between flake8-plone-hasattr and flake8-plone-api
  [iham]

1.3 (2017-05-31)
----------------
- added support for sublimetext (stdin/filename handling)
  [iham]

- Release universal wheels.
  [gforcada]

1.2 (2016-07-05)
----------------
- Fix the logic to report if a line has a replacement needed.
  Before the internal data got a parenthesis at the end there was some extra logic checking for end of line or a next character.
  But since some time ago a parenthesis was added as well,
  which made some checkers never report (namely getToolByName and probably lots more).
  [gforcada]

1.1 (2016-03-29)
----------------
- Remove ``restrictedTraverse`` as a suggestion to be replaced with get_view,
  there are way too many false positives.
  [gforcada]

1.0 (2016-03-01)
----------------
- Report which version of plone.api is needed to be able to apply
  each suggested replacement.
  [gforcada]

- Add methods from plone.api 1.5.
  [gforcada]

0.6 (2015-10-06)
----------------
- Instead of looking for catalog, look for .catalog, this
  should avoid some false positives
  [do3cc]

0.5 (2015-08-17)
----------------
- Improve testing so that physical files are no longer needed.
  [gforcada]

- Remove JSON data, use a regular python dictionary.
  [gforcada]

- Fix old approach being a substring of another method (getSite and getSiteManager).
  Fixes https://github.com/gforcada/flake8-plone-api/issues/1
  [gforcada]

- Improve test coverage.
  [gforcada]

0.4 (2015-08-16)
----------------
- Ignore ``XXX`` old usages, they are mostly a placeholder to keep the mapping
  easier.
  [gforcada]

0.3 (2015-08-16)
----------------
- I give up, collapse everything into a single file, should be easy...
  [gforcada]

0.2.post1 (2015-08-16)
----------------------
- Yet another try.
  [gforcada]

0.2.post0 (2015-08-16)
----------------------
- Still not...
  [gforcada]

0.2 (2015-08-16)
----------------
- All previous releases are broken, attempting to fix it
  (setuptools is playing with me).
  [gforcada]

0.1.post1 (2015-08-15)
----------------------
- Minor README enhancement.
  [gforcada]

0.1.post0 (2015-08-15)
----------------------
- Fix version number location.
  [gforcada]

0.1 (2015-08-15)
----------------
- Initial release
  [gforcada]

- Add buildout and other stuff.
  [gforcada]

- Add a ``mapping.json`` to add Plone API method calls to old usages data
  [gforcada]

- Add a ``mapping.py`` to convert ``mapping.json`` into a reverse mapping
  (to be used by the flake8 plugin).
  [gforcada]

- Create the flake8 plugin per se that iterates over the files and searches
  for old usages (coming from ``mapping.py``).
  [gforcada]

- Add tests and badges for travis and coveralls
  [gforcada]
