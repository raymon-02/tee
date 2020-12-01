# teec
### Implementation of _tee_ command in command-line interpreter

#### Requirements:
* [python3](https://www.python.org/downloads/) >= 3.7 must be installed and added to PATH
* [pip3](https://pip.pypa.io/en/stable/installing/) >= 3.0 must be installed and added to PATH


#### Run:
Usage of `teec` has no difference from linux `tee` console command
* usage 
```bash
teec [-a] [-i] [<file>...]
```
* get `help` 
```bash
teec --help
```

#### Run tests:
* install `pytest` package
```bash
pip3 install pytest
```
* run from root `teec` directory
```bash
python3 -m pytest tests/teec_tests.py
```
