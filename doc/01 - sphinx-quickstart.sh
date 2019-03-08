#!/bin/bash

pwd=`pwd`
#cd ../venv
#source bin/activate
cd $pwd
sphinx-quickstart
cat index.rst | sed 's/.. toctree::/.. toctree:: source\/modules/' > index.rst_copy
cat conf.py | sed 's/alabaster/sphinx_rtd_theme/' > conf.py_copy
rm -rf conf.py
rm -rf index.rst
mv conf.py_copy conf.py
mv index.rst_copy index.rst
mkdir html
#deactivate
