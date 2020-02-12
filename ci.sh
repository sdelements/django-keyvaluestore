#!/bin/bash
set -ev

if [ "${LINT}" = "true" ]; then
  pip install flake8==2.6.2
  make lint
fi

python setup.py install
pip install django=="${DJANGO}"
make test
