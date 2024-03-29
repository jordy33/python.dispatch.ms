[Python-Markdown][]
===================

[![Build Status][travis-button]][travis]
[![Coverage Status][codecov-button]][codecov]
[![Latest Version][mdversion-button]][md-pypi]
[![Python Versions][pyversion-button]][md-pypi]
[![BSD License][bsdlicense-button]][bsdlicense]
[![Code of Conduct][codeofconduct-button]][Code of Conduct]

[travis-button]: http://img.shields.io/travis/Python-Markdown/markdown.svg
[travis]: https://travis-ci.org/Python-Markdown/markdown
[codecov-button]: https://codecov.io/gh/Python-Markdown/markdown/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/Python-Markdown/markdown
[mdversion-button]: http://img.shields.io/pypi/v/Markdown.svg
[md-pypi]: http://pypi.python.org/pypi/Markdown
[pyversion-button]: http://img.shields.io/pypi/pyversions/Markdown.svg
[bsdlicense-button]: http://img.shields.io/badge/license-BSD-yellow.svg
[bsdlicense]: http://opensource.org/licenses/BSD-3-Clause
[codeofconduct-button]: https://img.shields.io/badge/code%20of%20conduct-contributor%20covenant-green.svg?style=flat-square
[Code of Conduct]: https://github.com/Python-Markdown/markdown/blob/master/CODE_OF_CONDUCT.md

This is a Python implementation of John Gruber's [Markdown][].
It is almost completely compliant with the reference implementation,
though there are a few known issues. See [Features][] for information
on what exactly is supported and what is not. Additional features are
supported by the [Available Extensions][].

[Python-Markdown]: https://Python-Markdown.github.io/
[Markdown]: http://daringfireball.net/projects/markdown/
[Features]: https://Python-Markdown.github.io#Features
[Available Extensions]: https://Python-Markdown.github.io/extensions

Documentation
-------------

Installation and usage documentation is available in the `docs/` directory
of the distribution and on the project website at
<https://Python-Markdown.github.io/>.

See the change log at <https://Python-Markdown.github.io/change_log>.

Support
-------

You may ask for help and discuss various other issues on the [mailing list][]
and report bugs on the [bug tracker][].

[mailing list]: http://lists.sourceforge.net/lists/listinfo/python-markdown-discuss
[bug tracker]: http://github.com/Python-Markdown/markdown/issues

Code of Conduct
---------------

Everyone interacting in the Python-Markdown project's codebases, issue trackers,
and mailing lists is expected to follow the [Code of Conduct].


# Device Registry Service

## Usage

All responses will have the form

```json
{
  "data":"Mixed type holding the content",
  "message":"Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all users

**Definition**

`GET /users`

**Response**

- `200 OK` on sucess
```json
[
  {
    "id":"identifier",
    "name":"Name of the person",
    "lastname":"Last Name",
    "gender":"Male, Female"    
  },
  {
    "id":"identifier",
    "name":"Name of the person",
    "lastname":"Last Name",
    "gender":"Male, Female"    
  }
]  
``` 
 
### Registering a new user

**Definition**

`POST /users'

**Arguments**

- `"identifier":string` a unique indentifier for this user 
- `"name":string` a name
- `"lastname":string` a last name
- `"gender":string` sex of the person

If a user already exists with  the given identifier, the existing user will be overwritten.

**Response**

- `201 Created` on success

```json
 {
    "id":"identifier",
    "name":"Name of the person",
    "lastname":"Last Name",
    "gender":"Male Female" 
 }
```
 