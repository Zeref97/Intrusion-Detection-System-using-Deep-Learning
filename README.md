# Intrusion Detection System using Deep Learning

Towards Developing a Network Intrusion Detection System using Deep Learning Techniques
- Published article: http://isyou.info/jisis/vol9/no4/jisis-2019-vol9-no4-01.pdf
- Modify based on: Deep Learning - IDS[https://github.com/rambasnet/DeepLearning-IDS]

## Introduction

In this project, we aim to explore the capabilities of various deep-learning frameworks in detecting
and classifying network intursion traffic with an eye towards designing a ML-based intrusion detection system.

## Dataset

-   Downloaded from: https://www.unb.ca/cic/datasets/ids-2018.html
-   used csv preprocessed and labelled files for this research project

## Usage:
### 1. Download data:
-   Install aws CLI.
-   Using the following syntax:
```
aws s3 cp --no-sign-request "s3://cse-cic-ids2018/Processed Traffic Data for ML Algorithms/" <dest-dir> --recursive
```

### 2. Cleanup data:
-   Using the following syntax to cleanup all data in the ids-2018 folder:
```
python3 data_cleanup.py all
```
-   Or cleanup single file:
```
python3 data_cleanup.py <PATH_DATA_INPUT> <PATH_DATA_OUTPUT>
```
-   The data output result will store in the CleanedTrafficData folder.


### 3. Deep Learning Frameworks

-   perfomance results using various deep learning frameworks are compared
-   10-fold cross-validation techniques was used to validate the model

#### 3.1. FastAI

-   https://www.fast.ai/
-   uses PyTorch, https://pytorch.org/ as the backend
-   Using the following syntax:
```
python3 fastai-expriments.py <PATH_CSV>
```

#### 3.2. Keras

-   Tensorflow:
```
python3 keras-tensorflow.py <PATH_CSV>
```
-   Theano:
```
python3 keras-theano.py <PATH_CSV>
```
-   CNTK:
```
python3 keras-cntk.py <PATH_CSV>
```

# References

1. Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani, “Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”, 4th International Conference on Information Systems Security and Privacy (ICISSP), Portugal, January 2018
