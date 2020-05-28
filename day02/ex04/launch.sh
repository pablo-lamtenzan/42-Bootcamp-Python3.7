#!/bin/bash

chmod +x build.sh
bash build.sh && pip install ./dist/ai42-1.0.0.tar.gz
#bash build.sh && pip install ./dist/ai42-1.0.0-py3-none-any.whl
# rm -rf ai42.egg-info build dist 