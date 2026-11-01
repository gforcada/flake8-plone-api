# Changelog

## 2.0.1 (unreleased)

- update supported python versions (3.11 to 3.15) @gforcada

- improve CI speed by using `uvx` and `prek` @gforcada

- tighten GHA with `zizmor` @gforcada

## 2.0.0 (2025-10-25)

- drop python 3.8 and add python 3.13 @gforcada

- drop python 3.9 support and add Python 3.14 support @gforcada

- bump pypy minimum version to 3.10 @gforcada

## 1.6.0 (2023-11-03)

- drop python 3.7 support @gforcada

- test against python 3.12 @gforcada

- use `pyproject.toml` rather than `setup.py` @gforcada

- switch from `setuptools` to `hatchling` @gforcada

- switch to `main` branch @gforcada

- use `tox` and `pre-commit` to ease project maintenance @gforcada

## 1.5.0 (2022-10-09)

- pin dependencies @gforcada

- test/QA with GitHub actions @gforcada

- overhaul testing @gforcada

## 1.4 (2017-05-31)

- Fixed false positive "default_language" string match. (issue #17) @iham

- Fix conflict between flake8-plone-hasattr and flake8-plone-api @iham

## 1.3 (2017-05-31)

- added support for sublimetext (stdin/filename handling) @iham

- release universal wheels @gforcada

## 1.2 (2016-07-05)

- fix the logic to report if a line has a replacement needed.
  Before the internal data got a parenthesis at the end
  there was some extra logic checking for end of line or a next character.
  But since some time ago a parenthesis was added as well,
  which made some checkers never report
  (namely `getToolByName` and probably lots more) @gforcada

## 1.1 (2016-03-29)

- remove `restrictedTraverse` as a suggestion to be replaced with `get_view`,
  there are way too many false positives @gforcada

## 1.0 (2016-03-01)

- report which version of `plone.api` is needed to be able to apply
  each suggested replacement @gforcada

- add methods from `plone.api` 1.5 @gforcada

## 0.6 (2015-10-06)

- instead of looking for catalog, look for .catalog, this
  should avoid some false positives @do3cc

## 0.5 (2015-08-17)

- improve testing so that physical files are no longer needed @gforcada

- remove JSON data, use a regular python dictionary @gforcada

- fix old approach being a substring of another method (`getSite` and `getSiteManager`).
  Fixes [#1](https://github.com/gforcada/flake8-plone-api/issues/1) @gforcada

- improve test coverage @gforcada

## 0.4 (2015-08-16)

- ignore `XXX` old usages, they are mostly a placeholder to keep the mapping
  easier @gforcada

## 0.3 (2015-08-16)

- I give up, collapse everything into a single file, should be easy.. @gforcada

## 0.2.post1 (2015-08-16)

- yet another try @gforcada

## 0.2.post0 (2015-08-16)

- still not.. @gforcada

## 0.2 (2015-08-16)

- all previous releases are broken, attempting to fix it
  (`setuptools` is playing with me) @gforcada

## 0.1.post1 (2015-08-15)

- minor README enhancement @gforcada

## 0.1.post0 (2015-08-15)

- fix version number location @gforcada

## 0.1 (2015-08-15)

- initial release @gforcada

- add buildout and other stuff @gforcada

- add a `mapping.json` to add Plone API method calls to old usages data @gforcada

- add a `mapping.py` to convert `mapping.json` into a reverse mapping
  (to be used by the flake8 plugin) @gforcada

- create the `flake8` plugin per se that iterates over the files and searches
  for old usages (coming from `mapping.py`) @gforcada

- add tests and badges for travis and coveralls @gforcada
