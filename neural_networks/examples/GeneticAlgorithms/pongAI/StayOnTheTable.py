import numpy as np
import sys
sys.path.insert(0, '../../../network')
from neuralNetwork import network

import matplotlib
matplotlib.use('TKAGG')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
IDX = 0
dt=.1

numGenerations = 50
populationSize = 50
mating_pool_size= populationSize/4
population = [network([5,100,1]) for i in range(populationSize)]




def getCost(n):
    # a = getCostOneIter(n)
    # print 'cost is '+str(a)
    t= 0
    for i in range(100):
        t+=getCostOneIter(n)
    # print t
    return(t/100.)
getCost = np.vectorize(getCost)
def getCostOneIter(n):
    # print 'evaluting a cost'
    global dt
    # n = network([3,10,1])
    r        = 0
    tInitial = 0
    v        = 0
    cost     = 0
    ball_position = np.array([0,0])
    ball_velocity = np.array([.3,(np.random.random()-.5)/.5])
    # ball_velocity = np.array([.3,.1])
    t=0
    while ball_position[0]<1 and t<200:
    # for i in range(10):
    # while True:
        ball_position,ball_velocity = updateBallPos(ball_position,ball_velocity,r)
        v = 2*(n.feedForward([ball_position[0],ball_position[1],ball_velocity[0],ball_velocity[1],r])[-1][0]-.5)
        r += v*dt

        r = min(r,1-.09)
        r = max(r,-1+.09)
        t+=dt
        # print t
    return t-np.abs(r-ball_position[1])

def YeildPath():
    dt = .1
    global n
    r        = 0
    tInitial = 0
    v        = 0
    cost     = 0
    ball_position = np.array([0,0])
    ball_velocity = np.array([.3,(np.random.random()-.5)/.5])
    # ball_velocity = np.array([.3,.1])
    path = []
    while ball_position[0]<1:
    # for i in range(10):
    # while True:
        ball_position,ball_velocity = updateBallPos(ball_position,ball_velocity,r)
        v = 2*(n.feedForward([ball_position[0],ball_position[1],ball_velocity[0],ball_velocity[1],r])[-1][0]-.5)
        r += v*dt

        r = min(r,1-.1)
        r = max(r,-1+.1)
        # t+=dt
        yield([.8,r],ball_position)
    # return -t

def updateBallPos(r,v,paddleY):
    global dt
    if r[0]<-1:# or r[0]>1:
        v[0]*=-1
        r[0] ==-.99
    if r[1]>1 or r[1]<-1:
        v[1]*=-1
        r[1] +=-r[1]/(10*np.abs(r[1]))
    if r[0]>.8 and r[0]<.82 and r[1]<paddleY+.1 and r[1]>paddleY-.1:
        v[0]*=-1
    v[1]+=-.9*dt
    r=r+(v)*dt
    return(r,v)


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



for year in range(numGenerations):
    costs = getCost(population)
    population = [x for (y,x) in sorted(zip(1./np.array(costs),population))]
    print 'year : '+str(year)+' score : '+str(getCost(population[0]))+' badscore : '+str(getCost(population[-1]))
    # mating_pool = costs[0:mating_pool_size]
    costs = sorted(getCost(population),reverse = True)
    viability =  np.array(costs[0:mating_pool_size])
    # print viability[0],getCost(population[0])
    viability = viability/np.sum(viability)
    
    for i in range(mating_pool_size):
        i2 = np.random.choice(range(mating_pool_size),p = viability)
        if i2 == i:
            i2 = i+1
        # print 'bread'+str(i)+'   '+str(i2)
        new_kids = breed(population[i],population[i2])

        population[-2-i] = new_kids[0]
        population[-1-i] = new_kids[1]



population.sort(key=lambda x: getCost(x),reverse = True)
n = population[0]
print "+++++++++++++++++++"
print getCost(n)
print getCost(population[0])




fig, ax = plt.subplots()

line, = ax.plot([],[],'o')
ax.set_ylim(-1, 1)
ax.set_xlim(-1, 1)


class paddle(object):
    """docstring for paddle"""
    def __init__(self, positio):
        super(paddle, self).__init__()
        self.length = length



def update(data):
    # global IDX
    data,ball = data
    paddleDotsX = np.ones(7)*data[0]
    paddleDotsY = np.linspace(-.1,.1,7)+data[1]
    x = np.append(paddleDotsX,ball[0])
    y = np.append(paddleDotsY,ball[1])
    line.set_xdata(x)
    line.set_ydata(y)
    # plt.savefig(str(IDX).zfill(5)+str(".png"))
    # IDX+=1
    return line,


def data_gen():
    global r,v
    while True:
        r,v = newtGrav(r,v)
        yield r

ani = animation.FuncAnimation(fig, update, YeildPath, interval=1)
plt.show()
