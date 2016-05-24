import numpy as np
import sys
sys.path.insert(0, '../../../network')
from neuralNetwork import network
import matplotlib
matplotlib.use("TKAGG")
import matplotlib.pyplot as plt





class creature(object):
    """docstring for creature"""
    def __init__(self, brain = None):
        super(creature, self).__init__()
        self.brain = brain
        self.r = np.zeros(2)
        self.v = np.ones(2)
        self.v/= np.sum(self.v*self.v)
        if brain == None:
            self.brain = network([4,10,2])
    def step(self):
        """r and v are python arrays"""
        info = self.r.tolist()+self.v.tolist()
        self.v += (self.brain.feedForward(info)[-1]-np.array([.5,.5]))*dt
        self.r += self.v*dt
        

numGenerations = 100
populationSize = 500
population = [creature() for i in range(populationSize)]
dt = .1


def collide(a,b):
    if np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)<10:
        return True
    return False

def breed(n1,n2):
    """ n1 and n2 are brains"""
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
    return([creature(brain = c1),creature(brain = c2)])

def getCost(n):
    "cost function to create a creature that goes toward some food point"
    n.r = np.zeros(2)
    n.v = np.ones(2)
    for i in range(100):
        n.step()
    cost = n.r[0]**2+n.r[0]**2
    return(cost)



for year in range(numGenerations):

    population.sort(key=lambda x: getCost(x))
    a = getCost(population[0])
    if year%10==0:
        print year
    print ''
    if a<.0001:
        print 'yahoo!'
        break
    children = breed(population[0].brain,population[1].brain)
    population[-1] = children[0]
    population[-2] = children[1]



population.sort(key=lambda x: getCost(x))




# import numpy as np
# import sys
# sys.path.insert(0, '../../../network')
# from neuralNetwork import network
# import matplotlib
# matplotlib.use("TKAGG")
# import matplotlib.pyplot as plt

# numGenerations = 100
# populationSize = 20
# population = [creature() for i in range(populationSize)]
# dt = 10









#!/usr/bin/env python

# import numpy as np
# import time
# import matplotlib
# matplotlib.use('TKAgg')
# from matplotlib import pyplot as plt


def iter2(individual):
    """ A simple random walk with memory """

    print getCost(individual)
    posX = []
    posY = []
    individual.r = np.zeros(2)
    individual.v = np.ones(2)
    for i in range(100):
        individual.step()
        posX.append(individual.r[0])
        posY.append(individual.r[1])
    plt.plot(posX,posY)
    # plt.show()
for individual in population:
    iter2(individual)
plt.show()
# def getPos(population):
#     pos = []
#     for individual in population:
#         posX.append(individual.r[0])
#         posY.append(individual.r[1])
#     return(posX,posY)

# def iter():
#     """ A simple random walk with memory """
#     while True:
#         posX,posY = np.random.random((2,populationSize))
#         posX = posX.tolist()
#         posY = posY.tolist()
#         for individual in population:
#             individual.step()
#             posX.append(individual.r[0])
#             posY.append(individual.r[1])
#         yield [posX,posY]


# def run(niter=1000, doblit=True):
#     """
#     Display the simulation using matplotlib, optionally using blit for speed
#     """

#     fig, ax = plt.subplots(1, 1)
#     ax.set_aspect('equal')
#     ax.set_xlim(-3, 3)
#     ax.set_ylim(-3, 3)
#     ax.hold(True)
#     rw = iter()
#     x, y = rw.next()

#     plt.show(False)
#     plt.draw()

#     if doblit:
#         # cache the background
#         background = fig.canvas.copy_from_bbox(ax.bbox)

#     points = ax.plot(x, y, 'o')[0]
#     tic = time.time()

#     for ii in xrange(niter):

#         # update the xy data
#         x, y = rw.next()
#         points.set_data(x, y)

#         if doblit:
#             # restore background
#             fig.canvas.restore_region(background)

#             # redraw just the points
#             ax.draw_artist(points)

#             # fill in the axes rectangle
#             fig.canvas.blit(ax.bbox)

#         else:
#             # redraw everything
#             fig.canvas.draw()

#     plt.close(fig)
#     print "Blit = %s, average FPS: %.2f" % (
#         str(doblit), niter / (time.time() - tic))

# if __name__ == '__main__':
#     run(doblit=False)
#     run(doblit=True)