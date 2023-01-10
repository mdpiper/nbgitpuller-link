#! /usr/bin/env bash
# An example of constructing a link through the nbgitpuller CLI.

HUB=https://lab.openearthscape.org
REPO=https://github.com/csdms/ivy
BRANCH=main
FILE=lessons/bmi/index.ipynb  # Note: escape space in path with backslash
INTERFACE=notebook

nbgitpuller-link --version
nbgitpuller-link --help

nbgitpuller-link \
    --jupyterhub-url=$HUB \
    --repository-url=$REPO \
    --branch=$BRANCH \
    --launch-path="$FILE" \
    --interface=$INTERFACE
