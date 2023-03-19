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

# Set default goal to not be dependent on sorting / ordering.
.DEFAULT_GOAL := help  # defined in .make/default-help.mak

# Source the env-vars in your .env, if that file exists.
-include .env

# include re-usable makefiles
-include .make/*.mk


.PHONY: install  ## full initial installation
install: create-dirs symlink-venv-dirs dotenv-install-from-example dotenv-set-basedir dotenv-set-flask-secret-key create-venv poetry-install


.PHONY: create-dirs-extra  ## create extra dirs
create-dirs-extra:
	mkdir -p var/data
	mkdir -p var/static

.PHONY: post-install  ## create extra dirs
post-install:
	bin/pip install -e var/src/autoadd_bindir
	bin/pip install -e var/src/autoread_dotenv
	bin/pip install -e var/src/libranet_logging
	bin/pip install -e var/src/sitecustomize-entrypoints


.PHONY: fix  ## run fixes
fix: black isort black