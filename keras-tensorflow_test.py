import csv
import os
import sys
import numpy as np
import pandas as pd
import operator

from keras.models import Sequential, load_model
from keras.utils.np_utils import to_categorical, normalize
import time

dataPath = 'CleanedTrafficData'

# Define label
LABELS = ['Benign', 'FTP-BruteForce', 'SSH-Bruteforce']

def loadData(fileName):
    dataFile = os.path.join(dataPath, fileName)
    pickleDump = '{}.pickle'.format(dataFile)
    if os.path.exists(pickleDump):
        df = pd.read_pickle(pickleDump)
    else:
        df = pd.read_csv(dataFile)
        df = df.dropna()
        df = shuffle(df)
        df.to_pickle(pickleDump)
    return df

def test(dataFile, modelPath):
    
    data = loadData(dataFile)
    data_y = data.pop('Label')
    data_x = normalize(data.values)

    # Load model
    model = load_model(modelPath)
    
    inputDim = np.array(data_x).shape
    print('inputdim = ', inputDim)

    # Reshape (79,) to (1,79). Get data from 0 to 1044750
    data_test = data_x[1].reshape(1,79)

    # Predict prob
    predict_prob = model.predict(data_test)[0]

    # Predict label
    predict_class = model.predict_classes(data_test)[0]

    print('predict prob = ', np.max(predict_prob))
    print('label = ', LABELS[predict_class])

    # Get label from 0 to 1044750
    print('true label = ', np.array(data_y)[1])
        
if __name__ == "__main__":
    test(sys.argv[1], sys.argv[2])