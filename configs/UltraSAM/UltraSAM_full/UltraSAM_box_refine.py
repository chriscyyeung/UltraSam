_base_ = ['../../_base_/datasets/sam_dataset_bbox_prompt.py', '../../_base_/models/sam_mask_refinement.py']

data_root = '/home/cyeung/projects/aip-medilab/cyeung/LumpNavPNGResMatched'

metainfo = dict(classes=('tumor',))

train_dataloader = dict(
    batch_size=8,
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img=''),
        ann_file='train.agnostic.noSmall.coco.json',
        metainfo=metainfo,
    ),
)

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='images'),
        ann_file='coco_annotations.json',
        metainfo=metainfo,
    ),
)

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='images'),
        ann_file='coco_annotations_nonempty.json',
        metainfo=metainfo,
    ),
)

orig_val_evaluator = _base_.val_evaluator
orig_val_evaluator['ann_file'] = '{}/coco_annotations.json'.format(data_root)
val_evaluator = orig_val_evaluator

orig_test_evaluator = _base_.test_evaluator
orig_test_evaluator['ann_file'] = '{}/coco_annotations_nonempty.json'.format(data_root)
orig_test_evaluator['metric'] = ['segm']
test_evaluator = orig_test_evaluator
