# See ../makefile

.PHONY: black  ## run black on python-files
black:
	- black src/ tests/


.PHONY: flake8  ## run flake8 on python-files
flake8:
	- flake8 src/ tests/
#	- poetry run flake8 src/ tests/


.PHONY: isort  ## run isort on python-files
isort:
	- isort --recursive --settings-path=pyproject.toml src/**/*.py tests/**/*.py
#	poetry run isort **/*.py


.PHONY: pylint ## run pylint on python-files
pylint:
	poetry run pylint src tests


.PHONY: mypy ## run mypy on python-files
mypy:
	poetry run mypy src tests