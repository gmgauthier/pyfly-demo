#!/usr/bin/env sh

python3 -m pip install pipenv
pipenv run ./install.sh
pipenv run python3 app/simple.py & PID=$!
pipenv run python3 -m pytest tests/test_hov.py --verbose --show-capture=all
kill -9 $PID
