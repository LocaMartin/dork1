# setup.py
from setuptools import setup, find_packages

setup(
    name="my-cli-tool",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "my-cli-tool=my_cli_tool.main:main"
        ]
    },
)
