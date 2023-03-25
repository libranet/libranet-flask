# See ../makefile

# Add virtualenv to PATH, same effect as activating the virtualenv
# VENV_BIN_DIR := $(shell pwd)/.venv/bin
VENV_BIN_DIR := $(shell poetry env info --path)/bin

export PATH := $(VENV_BIN_DIR):$(PATH)
