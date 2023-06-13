# Author: Ritaank Tiwari

import argparse
import os.path as osp
import subprocess
from loguru import logger

def create_parser():
    parser = argparse.ArgumentParser(description='Setup the directory structure for SOMA')
    parser.add_argument('--studies_path', type=str, help='The path to S: from your device', default='/mnt/S/')
    return parser

def copy_dirs(args):

    dirs = ['soma-root', 'smpl-fast-derivatives.tar.bz2', 'bpy-2.83-20200908.tar.bz2']

    for dir in dirs:
        path_to_dir_base = osp.join(args.studies_path, '_Repositories','soma-setup', dir)
        logger.info(f"copying {dir} from {path_to_dir_base} to .")
        try:
            subprocess.run(['cp', '-R', path_to_dir_base, '.'])
        except:
            logger.error(f'Could not find {dir}. Please check the path to the studies folder')
            return
    
        logger.success(f"Successfully copied {dir} to .")

def setup(args):
    copy_dirs(args)

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    setup(args)