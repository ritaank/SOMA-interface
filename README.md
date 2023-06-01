# Running SOMA experiments

## Setting up environment

1. Clone the environment `git clone https://github.com/ritaank/SOMA-interface.git` inside some parent folder. For this setup tutorial, we will assume the parent folder is `dev`. The path to the SOMA-interface folder is `dev/SOMA-interface`.
2. `cd SOMA-interface`
3. Run `python setup.py --studies_path='<path-to-S:>'`. The default path to the Studies drive is `/mnt/S`. If on WSL2, the Studies drive must be mounted in the WSL2 environment. TODO: write instructions on how to mount network drives.
4. Running the above code copies in necessary dependencies into your `SOMA-interface` folder, including a large `soma-root` folder.
5. Set up the conda environment `soma` with all necessary dependencies. Follow the steps in [`conda-env.md`](conda-env.md).
6. Zipped archives can be deleted: `rm -rf bpy-2.83-20200908.tar.bz2 smpl-fast-derivatives.tar.bz2` 
7. `conda activate soma`



## Auto-labelling unlabeled mocaps

1. Place unlabeled mocaps in a folder in `<custom-folder-name>/support_files/evaluation_mocaps/original`. For example, if the folder name is `<unlabeled-mocaps>`, the path is `<custom-folder-name>/support_files/evaluation_mocaps/original/<unlabeled-mocaps>`

2. From the parent experiment directory (custom-folder name), and inside the conda environment, run `python label_mocaps.py --data_source='<unlabeled-mocaps>'`. To control more individual settings for this soma, use the `get_soma_conf_file` function.