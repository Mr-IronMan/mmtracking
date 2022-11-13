# -*- encoding: utf-8 -*-
"""
# @Time    : 2022/11/11 下午4:49
# @Author  : Jianwei Yang
# @File    : transfer_anno.py
# @Project: mmtracking
"""
# -*- encoding: utf-8 -*-
"""
# @Time    : 2022/11/11 下午3:48
# @Author  : Jianwei Yang
# @File    : gen_satsot_infos.py
# @Project: mmtracking
"""

import argparse
import os
import os.path as osp
import shutil


def parse_args():
    parser = argparse.ArgumentParser(
        description='Transfer the right label files to ICPR dataset')
    parser.add_argument(
        '-r',
        '--right',
        help='root directory of right label files',
    )
    parser.add_argument(
        '-o',
        '--original',
        help='root directory of ICPR dataset',
    )
    parser.add_argument(
        '-d',
        '--datastyle',
        help='the datastyle of ICPR dataset(training or validation)'
    )
    return parser.parse_args()


def transfer_label_files(label_path, root_path, datastyle):
    datastyle = datastyle + " data"
    label_path = osp.join(label_path, datastyle)
    root_path = osp.join(root_path, datastyle)
    videos_list = os.listdir(root_path)
    videos_list = [
        x for x in videos_list if osp.isdir(osp.join(root_path, x))
    ]
    for videoname in videos_list:
        shutil.rmtree(osp.join(root_path, videoname, 'sot'))
        shutil.copytree(osp.join(label_path, videoname, 'sot'), osp.join(root_path, videoname, 'sot'))

    print("transfer done!")


def main():
    args = parse_args()
    transfer_label_files(args.right, args.original, args.datastyle)


if __name__ == '__main__':
    main()
