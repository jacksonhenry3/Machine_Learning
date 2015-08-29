import numpy as np
import sys
sys.path.insert(0, '../../network')
from neuralNetwork import network
import matplotlib.pyplot as plt

numGenerations = 100
populationSize = 100
population = [network([2,100,2]) for i in range(populationSize)]


def getPath(n,ri = [0,0],vi = [0,0],tFinal = 1,dt = .1):
    r        = [ri]
    tInitial = 0
    v        = [vi]
    cost     = 0
    i = 0
    while np.abs(r[-1][0])<1 and np.abs(r[-1][1])<1  and i<500:
        i+=1
        a = 10*(n.feedForward(r[-1])[-1]-.5)
        v.append(v[-1]+a*dt)
        r.append(r[-1]+v[-1]*dt)
    r = np.array(r)
    return(r)



def breed(n1,n2):
    c1 = []
    c2 = []
    for layer1,layer2 in zip(n1.layers,n2.layers):
        mask = np.rint(np.random.random(layer1.shape))

        inverse_mask = np.abs(mask-1)

        c = layer2*mask +layer1*inverse_mask
        x = np.random.randint(0,c.shape[0],20)
        y = np.random.randint(0,c.shape[1],20)
        c[x,y] = np.logical_not(c[x,y])
        c1.append(c)
        c = layer1*mask +layer2*inverse_mask
        x = np.random.randint(0,c.shape[0],20)
        y = np.random.randint(0,c.shape[1],20)
        c[x,y] = np.logical_not(c[x,y])
        c2.append(c)


    c1 = network('',layers = c1)
    c2 = network('',layers = c2)
    return([c1,c2])


def getCost(n):
    "cost function to create a creature that goes toward some food point"
    cost = 0
    r = getPath(n,ri = [.5,.5],vi = [.1,.1])
    cost+= r.shape[0]
    return(1./cost)



for year in range(numGenerations):

    population.sort(key=lambda x: getCost(x))
    a =getCost(population[0])
    print a
    if a<.002:
        break
    children = breed(population[0],population[1])
    population[-1] = children[0]
    population[-2] = children[1]



population.sort(key=lambda x: getCost(x))
n = population[0]

# for i in range(10):
r = getPath(n,ri = [.5,.5],vi = [.1,.1],dt = .01,tFinal = 10)
cost= np.linalg.norm(r[-1])
plt.plot(r[:,0],r[:,1])



# plt.plot(paths[0][:,0],paths[0][:,1],'o')

plt.show()
