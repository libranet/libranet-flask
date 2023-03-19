# See ../makefile


.PHONY: symlink-venv-dirs ## symlinks .venv-dirs to make bin/python work
symlink-venv-dirs:
	ln -sf .venv/bin ;\
	ln -sf .venv/lib ;\
	ln -sf .venv/pyvenv.cfg


.PHONY: create-dirs ## initialize dir-structure, create dirs
create-dirs:
	mkdir -p var ;\
	mkdir -p var/cache ;\
	mkdir -p var/cache/vscode ;\
	mkdir -p var/log ;\
	mkdir -p var/run ;\
	mkdir -p var/tmp


.PHONY: create-venv ## create virtual-env with specified python-version in .env
create-venv:
	poetry env use ${PYTHON_VERSION}

.PHONY: poetry-install ## run poetry install to create the virtualenv
poetry-install:
	poetry install



.PHONY: poetry-install-no-root ## run poetry install to create the virtualenv and install only the dependencies
poetry-install-no-root:
	poetry install --no-root


.PHONY: poetry-install-no-dev ## run poetry install without dev-dependencies
poetry-install-no-dev:
	poetry install --no-dev


.PHONY: poetry-install-no-root-no-dev ## run poetry install to create the virtualenv and install only the prd-dependencies
poetry-install-no-root-no-dev:
	poetry install --no-root --no-dev

.PHONY: poetry-update ## run poetry update to update your project-dependencies
poetry-update:
	poetry update


.PHONY: poetry-env-info ## run env info
poetry-env-info:
	poetry env info


.PHONY: poetry-export-requirements  ## generate a requirements.txt-file
poetry-export-requirements:
	poetry export --format requirements.txt --output requirements.txt


.PHONY: poetry-show  ## poetry show
poetry-show:
	poetry show -o


.PHONY: poetry-show-outdated  ## poetry show  --outdated
poetry-show-outdated:
	poetry show --outdated