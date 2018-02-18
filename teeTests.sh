#!/usr/bin/env bash

if type -p python3 >/dev/null 2>&1; then
    echo -e "Found python3 in PATH"
    PYTHON=python3
else
    echo "Error: no python3 found"
    exit 1
fi

${PYTHON} -m pytest -q ./tee/test.py