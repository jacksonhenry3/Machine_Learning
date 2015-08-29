from random import randint,random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('Lichtenstein_test.png')[:,:,0:3]*255
img =  img.astype('uint8')
from scipy.ndimage.filters import gaussian_filter1d

# img     = np.mean(img,axis = 2)
# imgplot = plt.imshow()
# plt.show()
y = img.shape[0]
x = img.shape[1]
z = img.shape[2]

class creature(object):
    """docstring for gene"""
    def __init__(self, val):
        super(creature, self).__init__()
        self.val = val
        self.get_cost()
    def mutate(self):
        if randint(0,10)>9:
            ix = randint(0,x-1)
            iy = randint(0,y-1)
            r = random()*256
            self.val[iy,ix] = (self.val[iy,ix]+r)%256
            # self.val = gaussian_filter1d(self.val ,1,axis = 1)
            # self.val = gaussian_filter1d(self.val ,1,axis = 0)

    def mate(self,other):
        mask = np.floor(np.random.random((y,x,z))*2)
        inverse_mask = np.abs(mask-1)
        children = []
        child1 =creature(self.val*mask+other.val*inverse_mask)
        children.append(child1)
        child2 = creature(other.val*mask+self.val*inverse_mask)
        children.append(child2)
        return(children)
    def get_cost(self):
        difference = np.abs(img-self.val)
        self.cost  = np.sum(difference)
        # print self.cost

def generate_creature():
    img =  np.random.random((75,75,3))
    # for i in range(500):
    #     img+=np.random.random((75,75,3))
    img/=np.max(img)
    img*=255
    img = img.astype('uint8')
    return(creature(img))


pop_size = 200
mating_pool_size = pop_size/4

population = [generate_creature() for j in range(pop_size)]
number_of_generations = 5000





for generation in range(number_of_generations):
    population.sort(key=lambda x: x.cost, reverse=False)
    mating_pool = population[0:mating_pool_size]
    viability = np.array([1/(c.cost+.000001)for c in mating_pool])
    viability = viability/np.sum(viability)
    print(population[0].cost,generation)
    # plt.imsave('image_'+str(generation).zfill(3),population[0].val.astype('uint8'))
    if population[0].cost == 0:
        break
    for i in range(mating_pool_size):
        i2 = np.random.choice(range(mating_pool_size),p = viability)
        if i2 == i:
            i2 = i+1
        new_kids = population[i].mate(population[i2])
        population[-2-i] = new_kids[0]
        population[-1-i] = new_kids[1]


    for c in population:
        c.mutate()
        c.get_cost()


r   = np.append(img,population[0].val,axis = 0).astype('uint8')


imgplot = plt.imshow(r)

plt.show()
