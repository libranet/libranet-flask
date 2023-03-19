# flake8: noqa: E402 (module level import not at top of file)
# pylint: disable=unused-import
# pylint: disable=wrong-import-position
# pylint: disable=invalid-name
"""IPython startup-file, outside of PYTHONPATH.

Files in this startup-folder will be run in lexicographical order,
so you can control the execution order of files with a prefix, e.g.::

    00-foo.py
    10-baz.py
    20-bar.py

return-statements are not allowed.
We avoid executing code when debugging in ipdb by checking on env-var IS_IPYTHON
which is set in sitecustomize.

"""
print(f"\nRunning {__file__}")

import urllib3

import requests

url = "https://example.com"
resp = requests.get(url, timeout=5)

# http = urllib3.PoolManager()
# resp = http.request("GET", url, timeout=3)
breakpoint()