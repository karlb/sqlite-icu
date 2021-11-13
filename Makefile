build:
	python3 -m build

upload:
	python3 -m twine upload dist/sqlite-spellfix-*.tar.gz

test-upload:
	python3 -m twine upload --repository testpypi dist/sqlite-spellfix-*.tar.gz

download-icu:
	wget https://www.sqlite.org/src/raw/ext/icu/icu.c?name=c2c7592574c08cd1270d909b8fb8797f6ea1f49e931e71dbcc25506b9b224580 -O icu.c
