# Nearest Neighbor as Reference: A Simple Way to Boost the Performance of Image Captioning

Created by Junhua Mao

### Introduction

This code provide a simple way to boost the performance of image captioning task by reranking the hypotheses sentences according to the annotation of nearest neighbor images in the training set.
We denote this method as consensus reranking for the rest of this document.

We take the [m-RNN model](www.stat.ucla.edu/~junhua.mao/m-RNN.html) as an example to generate the hypotheses descriptions of an image.

The details is described in an arXiv paper: Nearest Neighbor as Reference: A Simple Way to Boost the Performance of Image Captioning

### Citing m-RNN and consensus reranking

If you find consensus reranking or the features refined by m-RNN model useful in your research, please consider citing:

    @article{mao2014deep,
      title={Deep Captioning with Multimodal Recurrent Neural Networks (m-RNN)},
      author={Mao, Junhua and Xu, Wei and Yang, Yi and Wang, Jiang and Huangzhi, Heng and Yuille, Alan},
      journal={ICLR},
      year={2015}
    }
    
### Requirements
- python 2.7 (Need ackages of numpy, scipy, nltk. All included in [Anaconda](https://store.continuum.io/cshop/anaconda/))
- java 1.8.0
- [MS COCO caption toolkit](https://github.com/tylin/coco-caption)

### Basic installation (sufficient for the demo)
1. install [MS COCO caption toolkit](https://github.com/tylin/coco-caption)

2. Suppose that toolkit is install on $PATH_COCOCap and this package is install at $PATH_mRNN_CR. Create a soft link to COCOCap as follows:
  ```Shell
  cd $PATH_mRNN_CR
  ln -sf ./external/coco-caption $PATH_COCOCap
  ```
  
3. Setup the package (will download necessary data, including refined features of m-RNN, ~1.5G)
  ```Shell
  bash setup.sh
  ```
  
### Demo
Run cr_mRNN_demo.py or view cr_mRNN_demo.ipynb

### Additional data
1. run download_mRNN_cache.sh to get the consensus reranking sample results on MS COCO crVal set (should be the same after running cr_mRNN_demo.py) and the nearest images index for MS COCO test 2014. (totally ~1.1G)

2. run download_VGG_orignial_feature.sh to get the extracted feature from origianl [VGGnet](http://arxiv.org/abs/1409.1556) on MS COCO train, val and test2014 (totally ~2.1G)

For more information about the format of the data, please refer to the Readme.md file in folder image_features_mRNN, mscoco_anno_files, and hypotheses_mRNN
