# utils
### Repository with command-line utils 

#### List of utils:
* **grep_log** &#8722; multi-pattern _grep_ with aho-corasick search
* **teec** &#8722; implementation of _tee_ command 

#### Requirements:
* [python3](https://www.python.org/downloads/) >= 3.7 must be installed and added to PATH
* [pip3](https://pip.pypa.io/en/stable/installing/) >= 3.0 must be installed and added to PATH

#### Setup:
Setup script builds and installs python package with specified util
 
To setup util run 
```
./setup.sh <util_name>

# e.g.
./setup.sh grep_log
./setup.sh teec
```

Each util has `bin` folder with console script. Add this script to PATH  
E.g `grep_log` util has `grep_log` console script