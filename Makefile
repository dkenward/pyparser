init:
	# install all requirements
	pip install -r example-requirements.txt
test:
	py.test tests

.PHONY : develop build clean clean_pyc doc

clean:
	-python setup.py clean

clean_pyc:
	-find . -name '*.py[co]' -exec rm {} \;

build: 
	clean_pyc
	python setup.py build_ext --inplace

develop: build
	-python setup.py develop

doc:
	-rm -rf doc/build doc/source/generated
	cd doc; \
	python make.py clean; \
	python make.py html
	python make.py spellcheck