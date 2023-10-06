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

.PHONY: clean  ## pre-install the virtualenv
clean: 
	- rm -fr bin lib lib64 pyvenv.cfg
	- rm -fr .venv
	- rm -fr var


.PHONY: pre-install  ## pre-install the virtualenv
pre-install: create-venv


.PHONY: install  ## full initial installation
# install: create-dirs symlink-venv-dirs dotenv-install-from-example dotenv-set-basedir dotenv-set-flask-secret-key create-venv poetry-install ipython-symlink-to-ip
install: create-dirs dotenv-install-from-example dotenv-set-basedir dotenv-set-flask-secret-key poetry-install symlink-venv-dirs  ipython-symlink-to-ip


.PHONY: create-dirs-extra  ## create extra dirs
create-dirs-extra:
	mkdir -p var/run
	mkdir -p var/data
	mkdir -p var/static


.PHONY: post-install  ## post-install steps
post-install:


.PHONY: fix  ## run fixes
fix: black isort ruff-fix
