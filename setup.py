from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

project_url = "https://github.com/"
project_url += "lepisma/kram"

required = [
    "crayons",
    "docopt",
    "numpy",
    "tinydb",
    "tinydb-serialization",
    "ujson"
]

setup(
    name="kram",
    version="0.1.0",
    description="Experiment logger",
    long_description=readme,
    author="Abhinav Tushar",
    author_email="abhinav.tushar.vs@gmail.com",
    url=project_url,
    install_requires=required,
    entry_points={
        "console_scripts": ["kram=kram.command:cli"],
    },
    keywords="",
    packages=find_packages(),
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only"
    ))
