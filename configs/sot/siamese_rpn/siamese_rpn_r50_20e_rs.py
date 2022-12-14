# -*- encoding: utf-8 -*-
"""
# @Time    : 2022/11/10 下午4:46
# @Author  : Jianwei Yang
# @File    : siamese_rpn_r50_20e_all_otb100.py.py
# @Project: mmtracking
"""
_base_ = ['./siamese_rpn_r50_20e_lasot.py']

crop_size = 511
exemplar_size = 127
search_size = 255

# model settings
model = dict(
    test_cfg=dict(rpn=dict(penalty_k=0.4, window_influence=0.5, lr=0.4)))

data_root = 'data/'
train_pipeline = [
    dict(
        type='PairSampling',
        frame_range=100,
        pos_prob=0.8,
        filter_template_img=False),
    dict(type='LoadMultiImagesFromFile', to_float32=True),
    dict(type='SeqLoadAnnotations', with_bbox=True, with_label=False),
    dict(
        type='SeqCropLikeSiamFC',
        context_amount=0.5,
        exemplar_size=exemplar_size,
        crop_size=crop_size),
    dict(type='SeqGrayAug', prob=0.2),
    dict(
        type='SeqShiftScaleAug',
        target_size=[exemplar_size, search_size],
        shift=[4, 64],
        scale=[0.05, 0.18]),
    dict(type='SeqColorAug', prob=[1.0, 1.0]),
    dict(type='SeqBlurAug', prob=[0.0, 0.2]),
    dict(type='VideoCollect', keys=['img', 'gt_bboxes', 'is_positive_pairs']),
    dict(type='ConcatSameTypeFrames'),
    dict(type='SeqDefaultFormatBundle', ref_prefix='search')
]
# dataset settings
data = dict(
    samples_per_epoch=60000,
    train=dict(
        type='RandomSampleConcatDataset',
        dataset_sampling_weights=[1],
        dataset_cfgs=[
            # dict(
            #     type='SATSOTDataset',
            #     ann_file=data_root + 'SatSOT/annotations/SatSOT_infos.txt',
            #     img_prefix=data_root + 'SatSOT',
            #     pipeline=train_pipeline,
            #     split='train',
            #     test_mode=False),
            dict(
                type='ICPRDataset',
                ann_file=data_root + 'ICPR_dataset/annotations/icpr_train_infos.txt',
                img_prefix=data_root + 'ICPR_dataset',
                pipeline=train_pipeline,
                split='train',
                test_mode=False)
        ]),
    val=dict(
        type='SATSOTDataset',
        ann_file=data_root + 'SatSOT/annotations/SatSOT_infos.txt',
        img_prefix=data_root + 'SatSOT',
        split='val',
        only_eval_visible=False),
    test=dict(
        type='SATSOTDataset',
        ann_file=data_root + 'SatSOT/annotations/SatSOT_infos.txt',
        img_prefix=data_root + 'SatSOT',
        split='test',
        only_eval_visible=False))
