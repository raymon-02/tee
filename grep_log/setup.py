import setuptools

import grep_log

with open("README.md", "r") as handler:
    long_description = handler.read()

setuptools.setup(
    name="grep-log",
    version=grep_log.__version__,
    author=grep_log.__author__,
    author_email="ilia.orlov93@gmail.com",
    description="Util to grep patterns in files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raymon-02/utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux, Mac OS"
    ],
    python_requires=">=3.7",
    install_requires=[
        "pyahocorasick==1.4.0"
    ],
    tests_require=[
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "grep_log = grep_log.__main__:main",
        ],
    }
)
