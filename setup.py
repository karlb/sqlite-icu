import subprocess
from setuptools import setup, Extension  # type: ignore

# read the contents of README
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# adapted from https://stackoverflow.com/a/60893447/114926
def pkgconfig(package):
    kw = {}
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = subprocess.getoutput(
        'pkg-config --cflags --libs {}'.format(package))
    for token in output.strip().split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

icu = Extension("icu", sources=["icu.c"], **pkgconfig('icu-uc icu-i18n'))

setup(
    name="sqlite-icu",
    version="1.0",
    description="Loadable ICU extension for sqlite",
    py_modules=["sqlite_icu"],
    ext_modules=[icu],
    url="http://github.com/karlb/sqlite-icu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['wheel'],
)
