# See ../makefile

.PHONY: black  ## run black on python-files
black:
	- bin/black src/ tests/


.PHONY: flake8  ## run flake8 on python-files
flake8:
	- bin/flake8 src/ tests/


.PHONY: isort  ## run isort on python-files
isort:
	- bin/isort --settings-path=pyproject.toml src/**/*.py tests/**/*.py
#	poetry run isort **/*.py


.PHONY: pylint ## run pylint on python-files
pylint:
	bin/poetry run pylint src tests


.PHONY: mypy ## run mypy on python-files
mypy:
	bin/poetry run mypy src tests