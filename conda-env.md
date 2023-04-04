# Setting up SOMA conda environment

These instructions come from the original SOMA respository setup [instructions](https://github.com/nghorbani/soma), with minor modifications.

## Package Installation

Note: we install a newer pytorch version, since pytorch-LTS (which is used in the original instructions) is now deprecated.

```shell
sudo apt install libatlas-base-dev
sudo apt install libpython3.7
sudo apt install libtbb2

conda create -n soma python=3.7 
conda install -c conda-forge ezc3d

conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

```

## Part 1: Installing SOMA

```shell

conda activate soma
git clone https://github.com/ritaank/soma.git #forked from nghorbani/soma
cd soma
python -m pip install -r requirements.py
python setup.py develop

```

Note: running setup in develop mode allows for live changes to the soma package code. See more [here](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install).

### Installing SMPL fast derivatives

Unzip the tarball folder `smpl-fast-derivatives.tar.bz2` into your conda env's `site-packages` folder. The final directory should look like `anaconda3/envs/soma/lib/python3.7/site-packages/psbody/smpl`

First find the location of `site-packages`. In the environment, run `python -c 'import site; print(site.getsitepackages()[0])'`.
Then, using that path, run the following command:

```shell

tar -jxf smpl-fast-derivatives.tar.bz2 -C <path-to-site-packages>

```

### Install psbody-mesh library

First clone the psbody-mesh repository at [https://github.com/MPI-IS/mesh](https://github.com/MPI-IS/mesh). Then, `cd mesh`

As per the instructions in the mesh README, we first must install the Boost <http://www.boost.org>_ libraries.
Linux:

`sudo apt-get install libboost-dev`

or on macOS:

`brew install boost`

TODO: show how to find Boost include. Then, install using the makefile:

`BOOST_INCLUDE_DIRS=/path/to/boost/include make all`

Finally, install the python package:

`python setup.py install`

### Blender

To use the rendering capabilities, first install an instance of Blender-2.83 LTS on your machine. Afterwards, uncompress contents of the precompiled bpy-2.83 into your python site-packages folder, i.e. anaconda3/envs/soma/lib/python3.7/site-packages.

Unzip the tarball folder `bpy-2.83-20200908.tar.bz2` into your conda env's `site-packages` folder. After unzipping, there should be a folder at `anaconda3/envs/soma/lib/python3.7/site-packages/2.83` as well as a file at `anaconda3/envs/soma/lib/python3.7/site-packages/bpy.so`.

First find the location of `site-packages`. In the environment, run `python -c 'import site; print(site.getsitepackages()[0])'`.
Then, using that path, run the following command:

```shell

tar -jxf bpy-2.83-20200908.tar.bz2 -C <path-to-site-packages>

```

## Part 2: Installing MoSH++

These instructions come from the original Mosh++ [repository](https://github.com/nghorbani/moshpp), with minor modifications.

Ensure that you are still inside the same environment (soma).

```shell

sudo apt install libtbb-dev libeigen3-dev

git clone https://github.com/ritaank/moshpp.git
cd moshpp
python -m pip install -r requirements.txt
cd src/moshpp/scan2mesh
python -m pip install -r requirements.txt
cd mesh_distance
make
cd ../../../..
# We should be at the root of the moshpp folder
python setup.py develop

```