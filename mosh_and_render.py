import os
import os.path as osp
from glob import glob

from loguru import logger

from soma.amass.mosh_manual import mosh_manual

soma_work_base_dir = osp.join(os.getcwd(), 'soma-root') 
support_base_dir = osp.join(soma_work_base_dir, 'support_files')

mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/original')

work_base_dir = osp.join(soma_work_base_dir, 'running_just_mosh')
temp_base_dir = osp.join(support_base_dir, 'render_out_temp')

target_ds_names = ['immersion_tiny',]

def select(fname):
    '''
    Running MoSH takes time, so a filter can be applied if only a subset of mocaps is needed.
    '''
    # add filters here
    return True

for ds_name in target_ds_names:
    mocap_fnames = glob(osp.join(mocap_base_dir, ds_name,  '*/*.c3d'))

    mocap_fnames = list(filter(select, mocap_fnames))
    print(mocap_fnames)

    logger.info(f'#mocaps found for {ds_name}: {len(mocap_fnames)}')

    mosh_manual(
        mocap_fnames,
        mosh_cfg={
            'moshpp.verbosity': 1, # set to 2 to visualize the process in meshviewer
            'dirs.work_base_dir': osp.join(work_base_dir, 'mosh_results'),
            'dirs.support_base_dir': support_base_dir,
            'mosh_stagei_perseq': True,
        },
        render_cfg={
        
            'moshpp.verbosity': 1, # set to 2 to visulaize the process in meshviewer
            # 'render.render_only_one_image': True, # uncomment for initial testing of the pipeline
            'render.video_fps': 60,  # 25, #video_fps * ds_rate should equal the sample fps always
            'mesh.ds_rate': 4,
            'render.resolution.change_from_blend': True,
            'render.resolution.default': [1600, 1600],  # [x,y]
            'render.render_engine': 'eevee',  # eevee / cycles,
        
            'dirs.work_base_dir': osp.join(work_base_dir, 'mp4_renders'),
            'render.render_engine': 'eevee',  # eevee / cycles,
            # 'render.render_engine': 'cycles',  # eevee / cycles,
            'render.show_markers': True,
            'render.save_final_blend_file': True,
            'dirs.support_base_dir': support_base_dir,
            'dirs.temp_base_dir': temp_base_dir

        },
        parallel_cfg={
            'pool_size': 5,
            # 'max_num_jobs': 1,
            'randomly_run_jobs': True,
        },
        run_tasks=[
            'mosh',
            # 'render',
        ],
        fast_dev_run=False,
    )
