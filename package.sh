rm -rf dist
python3 setup.py sdist
twine upload --username ${USER} --password ${PWD}  dist/*