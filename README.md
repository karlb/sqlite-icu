# sqlite-icu

This python package includes a loadable `icu` extension module for sqlite. This allows other python packages to use this extension without requiring dependencies outside of the python ecosystem. For more details on the extension itself, see [the official documentation](https://www.sqlite.org/src/artifact?ci=trunk&filename=ext/icu/README.txt).

## Installation

### Latest Release

Install the `sqlite-icu` package from pypi.

### Current Development Version

Install via pip

```sh
pip install git+git://github.com/karlb/sqlite-icu
```

or add this to you requirements.txt:

```
git+git://github.com/karlb/sqlite-icu
```


## Usage

```python
import sqlite3
import sqlite_icu

conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)
conn.load_extension(sqlite_icu.extension_path().replace('.so',''))

# now use as described in https://www.sqlite.org/icu.html
assert conn.execute("SELECT upper('i', 'tr_TR')").fetchone() == ('İ',)
```
