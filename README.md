# Running SOMA experiments

## Setting up environment

1. Clone the environment `git clone https://github.com/ritaank/SOMA-setup.git`

2. `cd SOMA-setup`

3. Set up the conda environment `soma` with necessary dependencies (follow steps **here** (TODO)). Install necessary packages directly into the `SOMA-setup folder`.

4. `conda activate soma`

5. Run `python setup.py --studies_path='<path-to-S:>'`. The default Studies path is `/mnt/S`.

6. Setup will copy all necessary assets into the current folder. The next step is to set up the conda environment. Follow the instructions in the `conda-env.md` file.

## Auto-labelling unlabeled mocaps

1. Place unlabeled mocaps in a folder in `<custom-folder-name>/support_files/evaluation_mocaps/original`. For example, if the folder name is `<unlabeled-mocaps>`, the path is `<custom-folder-name>/support_files/evaluation_mocaps/original/<unlabeled-mocaps>`

2. From the parent experiment directory (custom-folder name), and inside the conda environment, run `python label_mocaps.py --data_source='<unlabeled-mocaps>'`. To control more individual settings for this soma, use the `get_soma_conf_file` function.