from random import randint,random
import scipy.misc
import numpy as np
import matplotlib
matplotlib.use("TKAGG")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('Lenna.gif')
img = scipy.misc.imresize(img,20)
# print img.shape
width = img.shape[1]/80.
img=np.mean(img[:,:,0:3],axis = 2)

# imgplot = plt.imshow(img,cmap='Greys_r')
N = 10
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

    def mate(self,other):
        mask = np.floor(np.random.random((N**2,N**2))*2)
        inverse_mask = np.abs(mask-1)
        children = []
        child1 =creature(self.val*mask+other.val*inverse_mask)
        children.append(child1)
        child2 = creature(other.val*mask+self.val*inverse_mask)
        children.append(child2)
        return(children)
    def get_cost(self):
        fig = plt.figure(figsize = (width,width))
        plt.axis('off')
        for row in xrange(N**2):
            for col in xrange(N**2):
                if row != col and self.val[row,col]==1:

                    x1 = row/N
                    y1 = (row%N)
                    x2 = col/N
                    y2 = (col%N)

                    plt.plot([x1,x2],[y1,y2],'k')

        fig.canvas.draw()
        # fig.tight_layout()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = np.mean(data.reshape(fig.canvas.get_width_height()[::-1] + (3,)),axis =2)

        cost = np.sum(np.abs(data-img))
        self.cost = cost
        plt.close()


def generate_creature():
    VertexEdgeAdjacencyMatrix = np.rint(np.random.random((N**2,N**2))/1.5)
    return(creature(VertexEdgeAdjacencyMatrix))

pop_size = 8
mating_pool_size = pop_size/4

population = [generate_creature() for j in range(pop_size)]
for i in population:
    print i.val
number_of_generations = 1





for generation in range(number_of_generations):
    population.sort(key=lambda x: x.cost, reverse=False)
    mating_pool = population[0:mating_pool_size]
    viability = np.array([1/(c.cost+.000001)for c in mating_pool])
    viability = viability/np.sum(viability)
    print(population[0].cost,generation)
    # plt.imsave('image_'+str(generation).zfill(3),population[0].val.astype('uint8'))
    # if population[0].cost == 0:
    #     break
    for i in range(mating_pool_size):
        i2 = np.random.choice(range(mating_pool_size),p = viability)
        if i2 == i:
            i2 = i+1
        new_kids = population[i].mate(population[i2])
        population[-2-i] = new_kids[0]
        population[-1-i] = new_kids[1]


    for c in population:
        # c.mutate()
        c.get_cost()


fig = plt.figure(figsize = (width,width))
plt.axis('off')

for row in xrange(N**2):
    for col in xrange(N**2):
        if row != col and population[0].val[row,col]==1:

            x1 = row/N
            y1 = (row%N)
            x2 = col/N
            y2 = (col%N)

            plt.plot([x1,x2],[y1,y2],'k')
fig.canvas.draw()
# fig.tight_layout()
data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
data = np.mean(data.reshape(fig.canvas.get_width_height()[::-1] + (3,)),axis =2)


r   = np.append(img,data,axis = 0).astype('uint8')


imgplot = plt.imshow(r)

plt.show()
