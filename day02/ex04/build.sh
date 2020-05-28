#!/bin/bash

pip install --user --upgrade setuptools wheel
pip install --user tqdm

# chmod +x ai42

python setup.py sdist bdist_wheel

# pip install ./dist/ai42-1.0.0-py3-none-any.whl

