from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="libretunes",
    version="0.1.0",
    author="FredXYZ-cmd",
    description="A modern, open-source music player for Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FredXYZ-cmd/LibreTunes",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pygobject>=3.42",
    ],
    entry_points={
        "console_scripts": [
            "libretunes=libretunes.main:main",
        ],
    },
)
