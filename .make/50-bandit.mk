# See ../makefile


.PHONY: bandit  ## run bandit
bandit:
	bandit --src --baseline etc/bandit-baseline.json


.PHONY: bandit-update-baseline  ## update bandit baseline
bandit-update-baseline:
	bandit --src --format json --output etc/bandit-baseline.json