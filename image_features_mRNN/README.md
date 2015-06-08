#Image features extracted by VGGnet and VGGnet features refined by the m-RNN model

This folder contains files of image feautures.
After run the bash file: 'download_img_feat.sh', you will find two files.
Each file is a dictionary whose key is the 'id' of an image and the item is the *k* dimensional features.
For feature extract from original VGGnet, the dimension is 4096.
For feature refined by the m-RNN model, the dimension is 1024.

1. 'VGG_feat_o_dct_mscoco_2014.npy': features extracted by the [VGGnet](http://arxiv.org/abs/1409.1556) for MS COCO train2014, val2014 and test2014. We download the model file from [caffe model zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo)
2. 'VGG_feat_mRNN_refine_dct_mscoco_2014.npy': features refined by the m-RNN model for MS COCO train2014, val2014 and test 2014.

For more details of the feature extraction process, please refer to the paper: []()
