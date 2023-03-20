#!/bin/bash

rm -rf temp
mkdir temp
curl https://download.is.tue.mpg.de/soma/tutorials/SOMA_FOLDER_TEMPLATE.tar.bz2 --output ./temp/SOMA_FOLDER_TEMPLATE.tar.bz2
tar -xjf ./temp/SOMA_FOLDER_TEMPLATE.tar.bz2 -C ./
mv SOMA_FOLDER_TEMPLATE $1


