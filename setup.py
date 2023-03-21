# Author: Ritaank Tiwari

# Todo, write ability to build the directory structure directly curling the MPI site

import argparse
import os
import subprocess

def create_parser():
    parser = argparse.ArgumentParser(description='Setup the directory structure for SOMA')
    parser.add_argument('-folder_name', type=str, help='Custom folder name for this experiment',)
    parser.add_argument('--studies_path', type=str, help='The path to S: from your device', default='/mnt/S/')
    return parser

def setup(args):
    path_to_soma_base = os.path.join(args.studies_path, '_Repositores', 'SOMA_BASE_FOLDER')
    subprocess.run(['cp', '-R', path_to_soma_base, '.'])
    subprocess.run(['mv', './SOMA_BASE_FOLDER', args.folder_name])
    subprocess.run(['cp', 'label_mocaps.py', './' + args.folder_name])
    subprocess.run(['cp', 'mosh_labeled_mocaps.py', './' + args.folder_name])

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    setup(args)