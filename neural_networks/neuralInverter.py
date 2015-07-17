import sys
sys.path.insert(0, './network')

from neural_network import *
import matplotlib.pyplot as plt

"""
Trains many neural networks in a row to inverst a binary array and calculates
the acuracy of that network and the creates a histogram of the acuracy.
"""

acuracy = []
length  = 15 # the length of the binary array

#each iteration generates and tests a neural network
for i in range(10):

    #generate the network
    inverter     = generate_neural_network([length,100,length])

    #generate some training data
    trainingData = []
    for i in range(int(2**length/50)):
        inData  = np.floor(np.random.random(length)*2)
        outData = np.abs(inData-1)
        trainingData.append([inData,outData])

    #give the network the training data
    inverter.train(trainingData,acceptableError = .1)

    #calculate how acutrate the netowrk is
    tot = 0
    for i in range(100):
        inData  = np.floor(np.random.random(length)*2)
        outData = np.abs(inData-1)
        inverter.feed_forward(inData)
        out = np.rint(inverter.get_output())
        if np.sum(np.abs(out-outData))==0:
            tot+=1

    print "Training complete, network is " +str(tot)+"% acurate"
    print '========================================================'
    print('\n')
    acuracy.append(tot/1.)
plt.hist(acuracy)
plt.show()
