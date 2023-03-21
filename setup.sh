#!/bin/bash

# rm -rf temp
# mkdir temp
# curl https://download.is.tue.mpg.de/soma/tutorials/SOMA_FOLDER_TEMPLATE.tar.bz2 --output ./temp/SOMA_FOLDER_TEMPLATE.tar.bz2
# tar -xjf ./temp/SOMA_FOLDER_TEMPLATE.tar.bz2 -C ./
# mv SOMA_FOLDER_TEMPLATE $1

curl https://download.is.tue.mpg.de/download.php?domain=smplx&sfile=smplx_locked_head.tar.bz2 --output ./temp/smplx_locked_head.tar.bz2
tar -xjf ./temp/smplx_locked_head.tar.bz2 -C ./$1/support_files/smplx
