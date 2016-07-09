#!/bin/sh
echo $TRAVIS_BUILD_DIR
echo "export PYTHONPATH=\$PYTHONPATH:\$TRAVIS_BUILD_DIR"
python $TRAVIS_BUILD_DIR/api/apiserver.py