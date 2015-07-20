import sys
sys.path.insert(0, './network')

from neural_network import *
import matplotlib.pyplot as plt

trainingData = []

values = [0,0,0,1,1,1,1,0]
prevStates = [[i,j,k] for i in range(2) for j in range(2) for k in range(2)]
prevStates =  np.array(prevStates)[::-1]
for i in range(8):
    trainingData.append([prevStates[i],[values[i]]])

automota = generate_neural_network([3,7,1])
automota.train(trainingData,acceptableError = .03)



initialState = np.zeros(101)
initialState[51] = 1
states = [initialState]

for i in range(400):
    print i
    nextState = [0]
    for j in range(1,len(initialState)-1):
        automota.feed_forward(input =initialState[j-1:j+2])
        nextState.append(automota.get_output()[0])
    nextState.append(0)
    nextState = np.rint(nextState)
    states.append(nextState)
    initialState = nextState

plt.imshow(states,interpolation = "none",cmap = 'gray')
plt.show()
