import inspect
import os
import sys
from pprint import pprint
from typing import Any

# file specific imports


target = 'index.py'
output = "AsylumLifeCrouchMacro.exe"

def resource_path(path: str, filename: str) -> str:
    return f"--include-data-dir=\"{os.path.abspath(path)}={filename}\""

def relative_resource_path(path: str, filename: str) -> str:
    return resource_path(os.path.join(os.path.dirname(__file__), "source", path), filename)

def module_resource_path(module: Any, path: str, filename: str) -> str:
    modulePath = os.path.dirname(inspect.getfile(module))
    return resource_path(os.path.join(modulePath, path), filename)

def icon(filename: str) -> str:
    return f"--windows-icon-from-ico=\"{os.path.join(os.path.dirname(__file__), 'source', filename)}\""

default_options = [
    sys.executable,
    "-m",
    "nuitka",
    f"\"{os.path.join(os.path.dirname(__file__), 'source', target)}\"",
    f"--output-dir=\"{os.path.dirname(__file__)}\"",
    f"--output-filename=\"{output}\"",
    "--onefile",
    "--standalone",
    "--assume-yes-for-downloads",
    "--deployment"
]

options = [
    "--warn-implicit-exceptions",
    "--warn-unusual-code",
    "--remove-output",
    "--no-pyi-stubs",
    "--python-flag=no_docstrings",
    "--company-name=verilisity",
    "--product-version=1.0",
    # "--mingw64",     # seems to cause virus warnings
]

def build():
    runOptions = default_options + options
    pprint(runOptions)
    os.system(" ".join(runOptions))

if __name__ == "__main__":
    build()