import sys
sys.path.insert(0, '../../network')
from neuralNetwork import network

import numpy as np
import matplotlib.pyplot as plt

trainingData = []

values = [0,0,0,1,1,1,1,0]
prevStates = [[i,j,k] for i in range(2) for j in range(2) for k in range(2)]
prevStates =  np.array(prevStates)[::-1]
for i in range(8):
    trainingData.append([prevStates[i],[values[i]]])

automota = network([3,7,1])
automota.train(trainingData)



initialState = np.zeros(301)
initialState[151] = 1
states = [initialState]

for i in range(300):
    # print i
    nextState = [0]
    for j in range(1,len(initialState)-1):
        out = automota.feedForward(initialState[j-1:j+2])
        nextState.append(out[-1][0])
    nextState.append(0)
    nextState = np.rint(nextState)
    states.append(nextState)
    initialState = nextState

plt.imshow(states,interpolation = "none",cmap = 'gray')
plt.show()
