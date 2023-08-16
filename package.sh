rm -rf dist
sed -i 's/@@@version@@@/$version/g' setup.py
python3 setup.py sdist
twine upload --username ${USER} --password ${PWD}  dist/*