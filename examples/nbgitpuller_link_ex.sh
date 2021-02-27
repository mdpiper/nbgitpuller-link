#! /usr/bin/env bash
# Example of constructing a link throug the nbgitpuller CLI.

HUB=https://csdms.rc.colorado.edu
REPO=https://github.com/csdms/espin
BRANCH=main
FILE=lessons/jupyter/index.ipynb

nbgitpuller-link --version
nbgitpuller-link --help

nbgitpuller-link \
    --jupyterhub-url=$HUB \
    --repository-url=$REPO \
    --branch=$BRANCH \
    --launch-path=$FILE
