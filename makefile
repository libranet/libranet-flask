# This is a comment.
# Important: You *must* indent using <TAB>s, not spaces.
#
# For more information, please see
#   - https://www.gnu.org/software/make/manual/make.html
#
# General syntax:
#   targets : prerequisites; recipes
#   <TAB>recipe
#
# - Commands starting with
#     "-" are ignoring their exit-code.
#     "@" do not echo the command itself.
#
# - make starts a new shell process for each recipe line.
#   Thus shell variables, even exported environment variables, cannot propagate upwards.
#   Therefore better concatenate your multiline-commands with ";\" into a single line.

# include re-usable makefiles
-include .make/*.mk


.PHONY: install  ## full initial installation
install: create-dirs symlink-venv-dirs dotenv-install-from-example dotenv-set-basedir dotenv-set-flask-secret-key create-venv poetry-install ipython-symlink-to-ip


.PHONY: create-dirs-extra  ## create extra dirs
create-dirs-extra:
	mkdir -p var/run
	mkdir -p var/data
	mkdir -p var/static


.PHONY: post-install  ## post-install steps
post-install:
	bin/pip install -e var/src/autoadd-bindir
	bin/pip install -e var/src/autoread-dotenv
	bin/pip install -e var/src/httpclient-logging
	bin/pip install -e var/src/libranet-logging
	bin/pip install -e var/src/sitecustomize-entrypoints


.PHONY: fix  ## run fixes
fix: black isort ruff-fix