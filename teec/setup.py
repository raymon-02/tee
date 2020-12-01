import setuptools

import teec

with open("README.md", "r") as handler:
    long_description = handler.read()

setuptools.setup(
    name="teec",
    version=teec.__version__,
    author=teec.__author__,
    author_email="ilia.orlov93@gmail.com",
    description="Custom implementation of tee util",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raymon-02/utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux, Mac OS"
    ],
    python_requires=">=3.7",
    tests_require=[
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "teec = teec.__main__:main",
        ],
    }
)
