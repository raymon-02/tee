#!/usr/bin/env bash

if type -p python3 >/dev/null 2>&1; then
    echo -e "Found python3 in PATH"
    PYTHON=python3
else
    echo "Error: no python3 found"
    exit 1
fi

if type -p pip3 >/dev/null 2>&1; then
    echo -e "Found pip3 in PATH"
    PIP=pip3
else
    echo "Error: no pip3 found"
    exit 1
fi

if [[ $# -gt 1 ]]; then
    echo "Wrong args number"
fi

echo -e "\nSetting run exec permission to tee and teeTests..."
chmod +x ./tee.sh
chmod +x ./teeTests.sh
echo -e "Set run exec permission to tee and teeTests"

echo -e "\nInstalling argparse package..."
${PIP} install argparse

if [[ $# -eq 1 ]]; then
    if [[ ${1} == "--test" ]] ; then
        echo -e "\nInstalling pytest package..."
        ${PIP} install pytest
    else
        echo -e "\nError: wrong test args name. Test argparse package is not installed"
        exit 1
    fi
fi