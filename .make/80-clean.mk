# See ../makefile


.PHONY: clean ## to remove all built documentation
clean:
	- rm -rf dist/
	@rm -rf build dist *.egg-info
	@find . -name '*.py?' -delete
