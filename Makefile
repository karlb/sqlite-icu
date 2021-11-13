build:
	python3 -m build

upload:
	python3 -m twine upload dist/sqlite-spellfix-*.tar.gz

test-upload:
	python3 -m twine upload --repository testpypi dist/sqlite-spellfix-*.tar.gz

download-icu:
	wget https://www.sqlite.org/src/raw/ext/icu/icu.c?name=91c021c7e3e8bbba286960810fa303295c622e323567b2e6def4ce58e4466e60 -O icu.c
