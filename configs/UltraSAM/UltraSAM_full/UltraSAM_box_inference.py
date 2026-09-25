_base_ = ['../../_base_/datasets/sam_dataset_inference.py', '../../_base_/models/sam_mask_refinement.py']

data_root = '/home/cyeung/projects/aip-medilab/cyeung/LumpNavPNGResMatched'

metainfo = dict(classes=('tumor',))

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img=''),
        ann_file='coco_stub.json',
        metainfo=metainfo,
    ),
)
