# -*- encoding: utf-8 -*-
"""
# @Time    : 2022/11/11 下午6:27
# @Author  : Jianwei Yang
# @File    : gen_icpr_infos.py
# @Project: mmtracking
"""

import argparse
import glob
import os
import os.path as osp
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate the information of ICPR dataset')
    parser.add_argument(
        '-i',
        '--input',
        help='root directory of ICPR dataset',
    )
    parser.add_argument(
        '-o',
        '--output',
        help='directory to save text file',
    )
    parser.add_argument(
        '-d',
        '--datatype',
        help='the datastyle of ICPR dataset(training or validation)'
    )
    return parser.parse_args()


def gen_data_infos(data_root, save_dir, datatype):
    """Generate dataset information.

    Args:
        data_root (str): The path of dataset.
        save_dir (str): The path to save the information of dataset.
    """
    print('Generate the information of ICPR dataset...')
    start_time = time.time()

    subdir = datatype
    videos_list = os.listdir(osp.join(data_root, subdir))
    videos_list = [
        x for x in videos_list if osp.isdir(osp.join(data_root, subdir, x))
    ]

    if not osp.isdir(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    videos_list = sorted(videos_list)
    with open(osp.join(save_dir, f'icpr_{datatype}_infos.txt'), 'w') as f:
        f.write('The format of each line in this txt is '
                '(video_path,annotation_path,start_frame_id,end_frame_id)')
        for video_name in videos_list:
            video_path = osp.join(datatype, video_name)

            ann_dir_path = osp.join(datatype, video_name, 'sot')
            ann_files = glob.glob(osp.join(data_root, ann_dir_path, '*.txt'))
            ann_files = sorted(ann_files, key=lambda x: int(osp.basename(x).split('.')[0].split('_')[0]))

            split_num = len(data_root)
            for ann_path in ann_files:
                start_frame_id = osp.basename(ann_path).split('.')[0].split('_')[1]
                end_frame_id = osp.basename(ann_path).split('.')[0].split('_')[2]
                ann_path_final = ann_path[split_num+1:]
                video_path_final = video_path + '/img1'

                f.write(f'\n{video_path_final},{ann_path_final},{start_frame_id},{end_frame_id}')

    print(f'Done! ({time.time() - start_time:.2f} s)')
    print(f'The results are saved in {save_dir}')


def main():
    args = parse_args()
    gen_data_infos(args.input, args.output, args.datatype)


if __name__ == '__main__':
    main()
