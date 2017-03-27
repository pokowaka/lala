#!/bin/sh
virtualenv venv
source venv/bin/activate
BASEDIR=$(dirname "$0")
PYTHONPATH=$BASEDIR:$PYTHONPATH

# install required packages
pip install matplotlib
pip install progressbar2 
 

