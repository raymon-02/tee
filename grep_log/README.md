# grep_log
### Multi-pattern command-line _grep_ with aho-corasick search

**_grep_log_** searches patterns in specified file 
or through all files in specified folder
and dumps result into result file

#### Requirements:
* [python3](https://www.python.org/downloads/) >= 3.7 must be installed and added to PATH
* [pip3](https://pip.pypa.io/en/stable/installing/) >= 3.0 must be installed and added to PATH

#### Run:
* search patterns in file
```bash
grep_log <file> <pattern> [<pattern>]
```
* search patterns through all files in folder
```bash
grep_log <file> <pattern> [<pattern>...]
```
* with specifying result folder (default is `<file>-greped`)
```bash
grep_log <file> <pattern> [<pattern>...]
```
* get help
```bash
grep_log --help
```

#### Run tests:
* install `pytest` package
```bash
pip3 install pytest
```
* run from root `grep_log` directory
```bash
python3 -m pytest tests/grep_log_tests.py
```
