# -*- encoding: utf-8 -*-
"""
# @Time    : 2022/11/11 下午3:48
# @Author  : Jianwei Yang
# @File    : gen_satsot_infos.py
# @Project: mmtracking
"""
import argparse
import glob
import os
import os.path as osp
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate the information of SatSOT dataset')
    parser.add_argument(
        '-i',
        '--input',
        help='root directory of SatSOT dataset',
    )
    parser.add_argument(
        '-o',
        '--output',
        help='directory to save text file',
    )
    return parser.parse_args()


def gen_data_infos(data_root, save_dir):
    """Generate dataset information.

    Args:
        data_root (str): The path of dataset.
        save_dir (str): The path to save the information of dataset.
    """
    print('Generate the information of SatSOT dataset...')
    start_time = time.time()

    videos_list = os.listdir(osp.join(data_root, 'test'))
    videos_list = [
        x for x in videos_list if osp.isdir(osp.join(data_root, 'test', x))
    ]

    if not osp.isdir(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    videos_list = sorted(videos_list)
    with open(osp.join(save_dir, f'SatSOT_infos.txt'), 'w') as f:
        f.write('The format of each line in this txt is '
                '(video_path,annotation_path,start_frame_id,end_frame_id)')
        for video_name in videos_list:
            video_path = osp.join('test', video_name)
            ann_path = osp.join('test', video_name, 'groundtruth.txt')
            img_names = glob.glob(osp.join(data_root, video_path, '*.jpg'))
            end_frame_name = max(
                img_names, key=lambda x: int(osp.basename(x).split('.')[0]))
            end_frame_id = int(osp.basename(end_frame_name).split('.')[0])
            f.write(f'\n{video_path},{ann_path},1,{end_frame_id}')

    print(f'Done! ({time.time() - start_time:.2f} s)')
    print(f'The results are saved in {save_dir}')


def main():
    args = parse_args()
    gen_data_infos(args.input, args.output)


if __name__ == '__main__':
    main()
