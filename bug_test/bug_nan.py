# -*- encoding: utf-8 -*-
"""
# @Time    : 2022/11/12 下午6:51
# @Author  : Jianwei Yang
# @File    : bug_nan.py
# @Project: mmtracking
"""
import os
import numpy as np

path = '/home/yangjianwei/mm/mmtracking/data/ICPR_dataset/train/001/sot'
for file_name in os.listdir(path):
    txt_path = path + '/' + file_name
    with open(txt_path) as f:
        for line in f:
            line_list = line.rstrip('\n').split(',')
            if len(line_list) != 4:
                print(file_name)
            for str in line_list:
                if str == '' or str == ' ':
                    print(file_name)
                    print(line_list)



