"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="aiopyarr",
    version="master",
    author="Robert Hillis",
    author_email="tkdrob4390@yahoo.com",
    description="An Asynchronous Lidarr, Radarr, Readarr, Sonarr APIs for Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tkdrob/aiopyarr",
    package_data={"aiopyarr": ["py.typed"]},
    packages=find_packages(include=["aiopyarr", "aiopyarr*"]),
    install_requires=["aiohttp>=3.6.1,<4.0"],
    keywords=["aiopyarr", "radarr", "sonarr", "plex"],
    license="MIT license",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
)
