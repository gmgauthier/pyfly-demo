#!/usr/bin/env sh

pipenv run python3 app/simple.py
pipenv run python3 -m pytest tests/test_hov.py --verbose --show-capture=all