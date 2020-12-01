#!/usr/bin/env bash

setup() {
    util_path=${HOME}/${1}
    if [[ ! -d "$util_path" ]]; then
        echo -e "ERROR: '$1' util is not found"
        return
    fi

    echo -e "'$1' util is found"
    cd ${util_path}

    echo -e "[$1] Setup..."

    echo -e "[$1] Building package..."
    ${PYTHON} setup.py bdist_wheel
    echo -e "[$1] Building completed"

    echo -e "[$1] Installing package..."
    ${PYTHON} -m pip install "dist/$util-$version-py3-none-any.whl"
    echo -e "[$1] Installing completed"

    echo -e "[$1] Setup completed\n"
    cd ..
}

PYTHON=python3
PIP=pip3
HOME=$(cd $(dirname ${0}) && pwd)

util=${1}
version="1.0"

setup ${util}
