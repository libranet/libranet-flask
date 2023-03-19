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

from sitecustomize._vendor.importlib_metadata import entry_points

from sitecustomize import most_recent_unique_entries

eps = entry_points(group="sitecustomize")

for ep in eps:
    print(f"{ep.name}: {ep.value}")

print("\n\nOrder of execution:")
for ep in most_recent_unique_entries(eps):
    print(f"\t{ep.name}: {ep.value}")
