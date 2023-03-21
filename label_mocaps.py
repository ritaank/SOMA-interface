import argparse
import os
import os.path as osp
import time

from soma.tools.run_soma_multiple import run_soma_on_multiple_settings

# Args for run_soma_on_multiple_settings:
#     soma_expr_ids: list of soma experiment ids
#     soma_mocap_target_ds_names: target dataset names, these should be available at mocap_base_dir
#     soma_data_ids: data ids of some experiments
#     tracklet_labeling_options: whether to use tracklet labeling
#     ds_name_gt: gt mocap data for labeling evaluation
#     soma_cfg: overloading soma_run_conf.yaml
#     mosh_cfg: overloading moshpp_conf.yaml inside mosh code
#     render_cfg: overload render_conf.yaml
#     eval_label_cfg: eval_label.yaml
#     parallel_cfg: relevant for use on IS cluster
#     fast_dev_run: if True will run for a limited number of mocaps
#     run_tasks: a selection of ['soma', 'mosh', 'render', 'eval_label']
#     mocap_ext: file extension of the source mocap point clouds
#     mosh_stagei_perseq: if True stage-i of mosh will run for every sequence instead of every subject
#     fname_filter: List of strings to filter the source mocaps
#     mocap_base_dir: base directory for source mocaps
#     gt_mosh_base_dir: directory holding mosh results of the gt mocaps, used for v2v evaluation
#     soma_work_base_dir: base directory for soma data. this directory holds: data, training_experiments, support_data
#     **kwargs:

def get_soma_conf_file():
    '''
    Prints path of soma_run_conf.yaml to inspect exact configuration settings
    '''
    import soma
    init_path = osp.join(soma.__file__)
    base_path = osp.dirname(init_path)
    conf_path = osp.join(base_path, 'conf', 'soma_run_path.yaml')

    print(conf_path)
    return conf_path


def solve_labels(args):
    '''
    For given folder, labels each mocap and outputs results into training_experiments folder
    '''

    soma_work_base_dir = os.getcwd()
    support_base_dir = osp.join(soma_work_base_dir, 'support_files')

    mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/original')
    timestr = time.strftime("%Y%m%d-%H%M%S")

    run_soma_on_multiple_settings(
        soma_expr_ids=[
            'V48_02_SuperSet', 
        ],
        soma_mocap_target_ds_names=[
            # 'immersion_tiny'
            args.data_source,
        ],
        soma_data_ids=[
            'OC_05_G_03_real_000_synt_100',
        ],
        soma_cfg={
            'mocap.subject_name' : f'{args.subject_name}_{timestr}',
            'soma.batch_size': 256,
            'dirs.support_base_dir':support_base_dir,
            'mocap.unit': 'mm',
            'save_c3d': True,
            # 'keep_nan_points': True,
            'remove_zero_trajectories': True,
            'mosh_stagei_perseq': True,
        },
        parallel_cfg={
            # 'max_num_jobs': 5,# comment to run on whole dataset
            'randomly_run_jobs': True,
        },
        run_tasks=[
            'soma',
        ],
        mocap_base_dir = mocap_base_dir,
        soma_work_base_dir=soma_work_base_dir,
        mocap_ext='.c3d'
    )

def create_parser():
    parser = argparse.ArgumentParser(description='Settings for a SOMA labelling run')
    parser.add_argument('-data_source', type=str, help='The name of the folder of the unlabeled mocap data',)
    parser.add_argument('--subject_name', type=str, help='the name of the subject', default="SubjectA")
    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    solve_labels(args)