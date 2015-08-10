from random import randint,random
import numpy as np
class creature(object):
    """docstring for gene"""
    def __init__(self, val):
        super(creature, self).__init__()
        self.val = val
        self.get_cost()
    def mutate(self):
        if randint(0,10)>3:
            idx = randint(0,12)
            r = random()
            if random>.5:
                n = 1
            else:
                n = -1
            self.val = self.val[:idx] + chr((ord(self.val[idx])-n)%256) + self.val[idx+1:]
            # self.val[idx] =
    def mate(self,other):
        idx = randint(0,12)
        children = []
        child1 = creature(self.val[0:idx]+other.val[idx:13])
        children.append(child1)
        children.append(creature(other.val[0:idx]+self.val[idx:13]))
        return(children)
    def get_cost(self):
        goal = 'Hello, World!'
        difference = [(ord(goal[i])-ord(self.val[i]))**2 for i in range(13)]
        self.cost = sum(difference)

def generate_creature():
    val = ''
    for i in range(13):
        r = randint(1,128)
        val+=chr(r)
    return(creature(val))


pop_size = 100
mating_pool_size = pop_size/4

population = [generate_creature() for j in range(pop_size)]
number_of_generations = 1000



for generation in range(number_of_generations):
    population.sort(key=lambda x: x.cost, reverse=False)
    mating_pool = population[0:mating_pool_size]
    viability = np.array([1/(float(c.cost)+.000001)for c in mating_pool])
    viability = viability/np.sum(viability)

    if population[0].cost == 0:
        break
    for i in range(mating_pool_size):
        luck = random()
from random import randint,random
import numpy as np
class creature(object):
    """docstring for gene"""
    def __init__(self, val):
        super(creature, self).__init__()
        self.val = val
        self.get_cost()
    def mutate(self):
        if randint(0,10)>2:
            idx = randint(0,12)
            r = random()
            if random>.5:
                n = 1
            else:
                n = -1
            self.val = self.val[:idx] + chr((ord(self.val[idx])-n)%256) + self.val[idx+1:]
            # self.val[idx] =
    def mate(self,other):
        idx = randint(0,12)
        children = []
        child1 = creature(self.val[0:idx]+other.val[idx:13])
        children.append(child1)
        children.append(creature(other.val[0:idx]+self.val[idx:13]))
        return(children)
    def get_cost(self):
        goal = 'Hello, World!'
        difference = [(ord(goal[i])-ord(self.val[i]))**2 for i in range(13)]
        self.cost = sum(difference)

def generate_creature():
    val = ''
    for i in range(13):
        r = randint(1,128)
        val+=chr(r)
    return(creature(val))


pop_size = 5000
mating_pool_size = pop_size/4

population = [generate_creature() for j in range(pop_size)]
number_of_generations = 1000


for generation in range(number_of_generations):
    population.sort(key=lambda x: x.cost, reverse=False)
    mating_pool = population[0:mating_pool_size]
    viability = np.array([1/(float(c.cost)+.000001)for c in mating_pool])
    viability = viability/np.sum(viability)
    print(population[0].val,population[0].cost)
    if population[0].cost == 0:
        break
    for i in range(mating_pool_size):
        luck = random()

        i2 = np.random.choice(range(mating_pool_size),p = viability)
        if i2 == i:
            i2 = i+1
        new_kids = population[i].mate(population[i2])
        population[-2-i] = new_kids[0]
        population[-1-i] = new_kids[1]


    for c in population:
        c.mutate()
        c.get_cost()
