# Setup file

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "flask",
    "requests"
]

setup(
    name="kram",
    version="0.0.2",
    description="",
    author="lepisma",
    author_email="abhinav.tushar.vs@gmail.com",
    url="https://github.com/lepisma/kram",
    include_package_data=True,
    install_requires=requirements,
    packages=[
        "kram",
    ],
    zip_safe=False,
    keywords="kram live plots"
)
