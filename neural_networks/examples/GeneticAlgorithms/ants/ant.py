import numpy as np
import sys
sys.path.insert(0, '../../../network')
from neuralNetwork import network
import matplotlib.pyplot as plt
from numpy.linalg  import  norm
from world import world

class ant(object):
    """docstring for ant"""
    def __init__(self, world, brain = None):
        super(ant, self).__init__()
        self.world = world
        self.brain = brain
        if brain == None:
            self.brain = network([5+200,100,2])
        self.energy = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.timeAlive = 0
        self.size = [1,2]
        self.mass = .1

    def updateEnergy(self):
        dt = self.world.timestep
        energyExpenditure = .5*self.mass*norm(self.velocity)**2*dt
        self.energy -= energyExpenditure

    def updatePosition(self):
        dt = self.world.timestep
        sensoryInformation = np.concatenate((self.position,self.velocity,[self.energy],self.world.foodPositions.flatten()))
        self.velocity = self.brain.feedForward(sensoryInformation)[-1]-.5
        if norm(self.velocity)<1:
            self.velocity/=norm(self.velocity)
        # print self.position
        # self.velocity+=acceleration*dt
        # self.velocity/=norm(self.velocity)
        self.position+=self.velocity*dt

    def update(self):
        dt = self.world.timestep
        if self.energy>0:
            self.timeAlive+=dt
            self.updateEnergy()
            self.updatePosition()
            closeToFood = norm(self.world.foodPositions-self.position,axis = 1)
            print closeToFood<1# self.velocity/=norm(self.velocity)
            if  np.any(closeToFood<1):
                self.energy = 1

    def breed(self,other):
        childsBrain = []
        for selfLayer,otherLayer in zip(self.brain.layers,other.brain.layers):
            shape = selfLayer.shape
            mask = np.rint(np.random.random(shape))
            inverseMask = np.abs(mask-1)
            childLayer = selfLayer*mask+otherLayer*inverseMask
            if np.random.random()>.95:
                x = np.random.randint(childLayer.shape[0])
                y = np.random.randint(childLayer.shape[1])
                childLayer[x,y] = np.random.randn()
            childsBrain.append(selfLayer*mask+otherLayer*inverseMask)
        return(ant(self.world,brain = network([],layers = childsBrain)))


earth = world(.1)


population = [ant(earth) for i in range(50)]
print 'goin'

n = False
for g in range(100):

    if n:
        break

    for a in population:
        x = []
        y = []
        i = 0
        a.position = (np.random.random((2))-.5)*20
        a.position = [0,0]
        a.velocity = [0,0]
        while a.energy >0 and i <1000:

            i+=1
            # if i>=1000:
            #     print "LIMIT"
            x.append(a.position[0])
            y.append(a.position[1])
            a.update()
        a.position = (np.random.random((2))-.5)*20
        a.velocity = [0,0]
        i = a.timeAlive
        if i>=1000.0:
            n = True
            break


    population.sort(key=lambda x: x.timeAlive, reverse=True)
    c = population[0].breed(population[1])
    print 'generation ' + str(g)+'. Best individual stayed alive for ' +str(population[0].timeAlive)
    population[-1] = c
    population[0].timeAlive = 0
    population[1].timeAlive = 0
    population[-1].timeAlive = 0
    population[0].energy = 1
    population[1].energy = 1
    population[-1].energy = 1

print "Done Training"

population.sort(key=lambda x: x.timeAlive, reverse=True)
# for a in population:

a.position = [0,0]
# for a in population:
a = population[0]
# a.position = (np.random.random((2))-.5)*20
a.velocity = [0,0]
a.timeAlive = 0
a.energy =1
x = []
y = []
i = 0
while a.energy >0 and i <10000:
    i+=1
    x.append(a.position[0])
    y.append(a.position[1])
    a.update()
plt.plot(x,y,'.')
print a.velocity

plt.plot(earth.foodPositions[:,0],earth.foodPositions[:,1],'o')
plt.show()
