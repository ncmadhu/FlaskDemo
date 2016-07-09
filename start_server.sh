#!/bin/sh
echo $TRAVIS_BUILD_DIR
echo "export CODE_HOME=$TRAVIS_BUILD_DIR/FlaskDemo"
echo $CODE_HOME
echo "export PYTHONPATH=\$PYTHONPATH:\$CODE_HOME"
python $TRAVIS_BUILD_DIR/FlaskDemo/api/apiserver.py