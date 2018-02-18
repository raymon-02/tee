#!/usr/bin/env bash

if type -p python3 >/dev/null 2>&1; then
    PYTHON=python3
else
    echo "Error: no python3 found"
    exit 1
fi

args=( "$@" )

${PYTHON} ./tee/tee.py ${args[@]}