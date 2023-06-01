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

Note: `python setup.py develop` uses the `setuptools` package to install SOMA as a python/pip package. Typically setup would either be run in either `install` or `develop` mode. Doing setup in develop mode allows for live changes to the soma package code. Otherwise, in `install mode`, every change would require a new `python setup.py install` to rebuild the pip package. See more [here](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install).

### Installing SMPL fast derivatives

SMPL fast derivatives provides code for computing the linear-blend skinning of the SMPL model, as well as code to operate a differentiable Rodrigues transform. It is necessary for the SOMA code to run.
We will unzip the tarball folder `smpl-fast-derivatives.tar.bz2` into your conda env's `site-packages` folder. The final directory should look like `anaconda3/envs/soma/lib/python3.7/site-packages/psbody/smpl`

To do this, first find the location of `site-packages`. In the environment, run `python -c 'import site; print(site.getsitepackages()[0])'`.
Then, using that path, run the following command:

```shell
tar -jxf smpl-fast-derivatives.tar.bz2 -C <path-to-site-packages>
rm smpl-fast-derivatives.tar.bz2
```

### Install psbody-mesh library

Clone the [psbody-mesh](https://github.com/MPI-IS/mesh) repository.

```shell
git clone https://github.com/MPI-IS/mesh.git
cd mesh
```

As per the instructions in the mesh [README](https://github.com/MPI-IS/mesh/blob/master/README.md), we first must install the Boost <http://www.boost.org>_ libraries.

Linux: `sudo apt-get install libboost-dev`
macOS: `brew install boost`

On Linux, the path to the boost 'include' directory should be `usr/include/boost`. With boost installed, we can finally make the mesh package, while passing in the location to the boost 'include' directory as an environment variable.

```shell
# Ensure that you are still in the mesh directory
`BOOST_INCLUDE_DIRS=/usr/include/boost make all` #or the path to boost 'include' on your specific machine
```

If there are issues in installing the mesh library, please refer to the links in this [issue](https://github.com/nghorbani/soma/issues/21).

Finally, install the python package:

```shell
`python setup.py install`
```

### Blender

To use the rendering capabilities, first install an instance of Blender-2.83 LTS on your machine. This can be done on the Blender [website](https://www.blender.org/download/).

Next, uncompress contents of the precompiled blender python `bpy-2.83` tarball into your python site-packages folder, i.e. `anaconda3/envs/soma/lib/python3.7/site-packages`. Follow steps below.

A tarball `bpy-2.83-20200908.tar.bz2` should exist in the `SOMA-interace` folder. Unzip this tarball into your `soma` conda env's `site-packages` folder. After unzipping, there should be a folder at `anaconda3/envs/soma/lib/python3.7/site-packages/2.83` as well as a file at `anaconda3/envs/soma/lib/python3.7/site-packages/bpy.so`.

First find the location of `site-packages`. In the environment, run `python -c 'import site; print(site.getsitepackages()[0])'`.
Then, using that path, run the following command:

```shell
tar -jxf bpy-2.83-20200908.tar.bz2 -C <path-to-site-packages>
rm bpy-2.83-20200908.tar.bz2
```

## Part 2: Installing MoSH++

These instructions come from the original Mosh++ [repository](https://github.com/nghorbani/moshpp), with minor modifications.

Ensure that you are still inside the same environment (`soma`).

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

## Part 3: Jupyter Notebook setup

```shell
# In environment `soma`
python -m pip install ipywidgets
conda install -c anaconda ipykernel
conda -install -n soma ipykernel --update-deps --force-reinstall
```

Now that the environment is fully set up, refer back to the README for instructions on how to run the SOMA code to label, MoSH, or render.
