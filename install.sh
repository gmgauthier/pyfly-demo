#!/usr/bin/env sh

OS=$(uname)
PY=$(which python3)
HC=$(which hoverctl)

echo "PREPARING PYTHON3 ENVIRONMENT..."
if [[ "$PY" = "python3 not found" ]];
    then
        echo "No python3 installation found. Attempting install now..."
        if [[ "$OS" = "Darwin" ]]; then
            $(brew install python3)
        fi
        if [[ "$OS" = "Linux" ]]; then
            $(sudo apt install python3)
        fi
        PY=$(which python3)
fi

echo "PREPARING HOVERFLY INSTALLATION..."
# shellcheck disable=SC2039
if [[ "$HC" = "hoverctl not found" ]];
    then
        echo "HoverFly CLI binary not found. Attempting install now..."
        if [[ "$OS" = "Darwin" ]]; then
            $(brew install hoverfly)
        fi
        if [[ "$OS" = "Linux" ]]; then
            $(wget https://github.com/SpectoLabs/hoverfly/releases/download/v1.0.0/hoverfly_bundle_linux_amd64.zip)
            $(unzip hoverfly_bundle_linux_amd64.zip)
            $(sudo mv hoverctl /usr/local/bin)
            $(sudo mv hoverfly /usr/local/bin)
        fi
        HC=$(which hoverctl)
fi

echo "PREPARING PROJECT VIRTUAL ENVIRONMENT..."
PENV=$(${PY} -m pip freeze|grep -i pipenv)
PYVER=$(${PY} --version)
echo "${PYVER}"

if [[ -z "$PENV" && "$PENV"=" " ]];
    then
        echo "Installing pipenv for python3..."
        ${PY} -m pip install pipenv
        echo "Installing pipenv virtual environment..."
        pipenv install
    else
        echo "\t${PENV}"
fi
echo "Dependency Graph:"
pipenv graph

echo "ALL SYSTEMS GO!"