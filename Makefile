.PHONY: virtualenv install pflake8 test

virtualenv:
	pip install --user pipenv
	pipenv shell

install:
	@echo "Hidded Installing..."
	echo "Installing..."
	pipenv install

lint:
	pflake8

format:
	isort controller migrations persistency view utils
	black controller migrations persistency view utils