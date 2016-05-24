from random import randint,random
import scipy.misc
import numpy as np
import matplotlib
matplotlib.use("TKAGG")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('Lenna.gif')
img = scipy.misc.imresize(img,100)
# print img.shape
width = img.shape[1]/80.
img=np.mean(img[:,:,0:3],axis = 2)

N = 10
guess = np.zeros((N**2,N**2))
lowestCost = 100000
for i in range(10):
    print i
    
    row = np.random.randint(N**2)
    col = np.random.randint(N**2)
    if guess[col,row] == 0:
        guess[col,row] = 1

        fig = plt.figure(figsize = (width,width))
        plt.axis('off')
        for rowi in xrange(N**2):
            for coli in xrange(N**2):
                if rowi != coli and guess[rowi,coli]==1:

                    x1 = rowi/N
                    y1 = (rowi%N)
                    x2 = coli/N
                    y2 = (coli%N)

                    plt.plot([x1,x2],[y1,y2],'k')

        fig.canvas.draw()
        # fig.tight_layout()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')

        data = np.mean(data.reshape(fig.canvas.get_width_height()[::-1] + (3,)),axis =2)
        # print data
        plt.close()
        cost = np.sum(np.abs(data-img))
        # print cost,lowestCost
        if cost < lowestCost:
            lowestCost = cost
            # print lowestCost
        else:
             guess[col,row] = 1



fig = plt.figure(figsize = (width,width))
plt.axis('off')
plt.imshow(img,cmap='Greys_r')
for rowi in xrange(N**2):
    for coli in xrange(N**2):
        if rowi != coli and guess[rowi,coli]==1:

            x1 = rowi/N*img.shape[1]/N
            y1 = (rowi%N)*img.shape[1]/N
            x2 = coli/N*img.shape[1]/N
            y2 = (coli%N)*img.shape[1]/N

            plt.plot([x1,x2],[y1,y2],'k')

# fig.canvas.draw()
# # fig.tight_layout()
# data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
# data = np.mean(data.reshape(fig.canvas.get_width_height()[::-1] + (3,)),axis =2)
# imgplot = plt.imshow(data,cmap='Greys_r')

plt.show()