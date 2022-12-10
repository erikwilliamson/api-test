#!/bin/bash

# Need this to update pyproject.toml
pip install --upgrade $(pip freeze | awk '{ print $1 }')
