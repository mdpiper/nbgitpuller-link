.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	rm -f setup.py

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 nbgitpuller_link examples tests

pretty: ## reformat files to make them look pretty
	find nbgitpuller_link examples tests -name '*.py' | xargs isort
	black nbgitpuller_link examples tests

test: ## run tests quickly with the default Python
	pytest --disable-warnings -vvv

coverage: ## check code coverage quickly with the default Python
	pytest --cov --cov-report=html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs and link check
	rm -f docs/source/api/nbgitpuller_link.rst
	rm -f docs/source/api/modules.rst
	sphinx-apidoc -o docs/source/api nbgitpuller_link
	pandoc --to=rst README.md > docs/source/README.rst
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(MAKE) -C docs linkcheck
	$(BROWSER) docs/build/html/index.html

setup: ## generate a setup.py file for release tools
	echo "import setuptools" >> setup.py
	echo "setuptools.setup()" >> setup.py

dist: clean setup ## build and package a release
	python -m build
	ls -l dist
	twine check dist/*

testpypi: dist ## upload a release to TestPyPI
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi: dist ## upload a release to PyPI
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

prerelease: clean setup ## generate a prerelease with zest.releaser
	prerelease

fullrelease: clean setup ## generate a full release with zest.releaser
	fullrelease

install: clean ## install the package to the active Python's site-packages
	pip install -e .
