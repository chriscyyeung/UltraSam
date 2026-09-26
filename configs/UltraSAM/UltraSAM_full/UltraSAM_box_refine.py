_base_ = ['../../_base_/datasets/sam_dataset_bbox_prompt.py', '../../_base_/models/sam_mask_refinement.py']

data_root = '/home/cyeung/projects/aip-medilab/cyeung/LumpNavPNGResMatchedCV/fold_4'

metainfo = dict(classes=('tumor',))

train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='train/images'),
        ann_file='train/coco_annotations.json',
        metainfo=metainfo,
    ),
)

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='val/images'),
        ann_file='val/coco_annotations.json',
        metainfo=metainfo,
    ),
)

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='val/images'),
        ann_file='val/coco_annotations.json',
        metainfo=metainfo,
    ),
)

orig_val_evaluator = _base_.val_evaluator
orig_val_evaluator['ann_file'] = '{}/val/coco_annotations.json'.format(data_root)
val_evaluator = orig_val_evaluator

orig_test_evaluator = _base_.test_evaluator
orig_test_evaluator['ann_file'] = '{}/val/coco_annotations.json'.format(data_root)
orig_test_evaluator['metric'] = ['segm']
orig_test_evaluator['outfile_prefix'] = './results/fold4_preds'
test_evaluator = orig_test_evaluator
