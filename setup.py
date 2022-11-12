from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="untable",
    version=0.1,
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/ubalklen/untable",
    },
    py_modules=[
        "untable",
    ],
    install_requires=[
        "beautifulsoup4",
    ],
)
