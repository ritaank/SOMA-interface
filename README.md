# Running SOMA experiments

## Setting up environment

1. Clone the environment `git clone https://github.com/ritaank/SOMA-setup.git`

2. `cd SOMA-setup`

3. Set up the conda environment `soma` with necessary dependencies (follow steps **here** (TODO)). Install necessary packages directly into the `SOMA-setup folder`.

4. `conda activate soma`

5. Run `python setup.py --folder_name='<custom-folder-name>' --studies_path='<path-to-S:>'`

6. Running `setup.py` will create a new folder called `<custom-folder-name>`, and will copy the scripts `label_mocaps.py` and `mosh_labeled_mocaps.py` into this custom folder. As setup is now complete, all following code and work should be done in our experiment folder.

7. `cd <custom-folder-name>`

## Auto-labelling unlabeled mocaps

1. Place unlabeled mocaps in a folder in `<custom-folder-name>/support_files/evaluation_mocaps/original`. For example, if the folder name is `<unlabeled-mocaps>`, the path is `<custom-folder-name>/support_files/evaluation_mocaps/original/<unlabeled-mocaps>`

2. From the parent experiment directory (custom-folder name), and inside the conda environment, run `python label_mocaps.py --data_source='<unlabeled-mocaps>'`. To control more individual settings for this soma, use the `get_soma_conf_file` function.