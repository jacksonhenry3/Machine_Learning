import sys
sys.path.insert(0, '../../network')
from neuralNetwork import network

import numpy as np
import matplotlib.pyplot as plt

"""
Trains many neural networks in a row to invert a binary array and calculates
the acuracy of that network and the creates a histogram of the acuracy.
"""

acuracy = []
length  = 10 # the length of the binary array

#each iteration generates and tests a neural network
for i in range(2):

    #generate the network
    inverter     = network([length,100,length])

    #generate some training data
    trainingData = []
    # for i in range(int(2**length/25)):
    for i in range(5):
        inData  = np.floor(np.random.random(length)*2)
        outData = np.abs(inData-1)
        trainingData.append([inData,outData])
    # print train
    #give the network the training data
    inverter.train(trainingData)

    #calculate how acutrate the netowrk is
    tot = 0
    for i in range(1000):
        inData  = np.floor(np.random.random(length)*2)
        outData = np.abs(inData-1)
        out = np.rint(inverter.feedForward(inData)[-1])
        if np.sum(np.abs(out-outData))==0:
            tot+=1

    print "Training complete, network is " +str(tot/10.)+"% acurate"
    print '========================================================'
    print('\n')
    acuracy.append(tot/10.)
plt.hist(acuracy)
plt.show()
