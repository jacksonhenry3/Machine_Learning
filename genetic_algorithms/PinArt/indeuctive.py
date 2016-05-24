from random import randint,random
import scipy.misc
import numpy as np
import matplotlib
matplotlib.use("TKAGG")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

lowestCost = 10000000**100

img = mpimg.imread('Lenna.gif')
img = mpimg.imread('bob.JPG')
img = mpimg.imread('ruby.JPG')
img = scipy.misc.imresize(img,25)
img = np.mean(img[:,:,0:3],axis = 2)

# low_values_indices = img < 55  # Where values are low
# img[low_values_indices] = 0  # All low values set to 0
# low_values_indices = img >= 55  # Where values are low
# img[low_values_indices] = 255  # All low values set to 0

plt.imshow(img)
plt.show()

width = img.shape[1]/80.
height = img.shape[0]/80.

# bestFigure = plt.figure()
fig = plt.figure(figsize = (width,height))
plt.axis('off')
# bestAxes = bestFigure.add_subplot(1, 1, 1)
ax = fig.add_subplot(1, 1, 1)

N = 100
guess  = np.zeros((N**2,N**2))

for i in range(10000):
    print i
    row = np.random.randint(N**2)
    col = np.random.randint(N**2)
    if (guess[col,row] == 0) and( col != row) and (guess[row,col] ==0):
        guess[col,row] = 1

        x1 = row/N
        y1 = (row%N)
        x2 = col/N
        y2 = (col%N)
        line = ax.plot([x1,x2],[y1,y2],'k')

        fig.canvas.draw()
        # fig.tight_layout()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = np.mean(data.reshape(fig.canvas.get_width_height()[::-1] + (3,)),axis =2)
        cost = np.sum(np.abs(data-img))
        if cost < lowestCost:
            lowestCost = cost
            # print lowestCost
        else:
            guess[col,row] = 0
            line.pop(0).remove()
    
plt.show()



# ax.imshow(img)
# plt.show()