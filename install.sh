#!/usr/bin/env bash

# Just create a folder in home cause
mkdir /opt/mhall
cp -r ./mhall /opt/mhall
cp ./cli.py /opt/mhall
ln -s /opt/mhall/cli.py $HOME/bin/mhall

