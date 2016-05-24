import numpy as np
import matplotlib
matplotlib.use("TKAGG")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=np.mean(mpimg.imread('Lenna.gif')[:,:,0:3],axis = 2)
# imgplot = plt.imshow(img,cmap='Greys_r')
# plt.show()

imgWidth = 3
N = 8

# ratio = 10

# fig = plt.figure()
# fig.add_subplot(111)
bestScore = 10**100
w, h = plt.figaspect(1.)
fig = plt.figure(figsize = (2.1,2.1))

# plt.set_aspect('equal')
# plt.set_xlim(0,1)
# plt.set_ylim(0,1)
plt.axis('off')
for i in range(5):
	
	exampleGenome = np.rint(np.random.random((N**2,N**2))/1.9)
	# print exampleGenome
	for row in xrange(N**2):
		for col in xrange(N**2):
			if row != col and exampleGenome[row,col]==1:

				x1 = row/N
				y1 = (row%N)
				x2 = col/N
				y2 = (col%N)

				plt.plot([x1,x2],[y1,y2],'k')

	fig.canvas.draw()
	fig.tight_layout()
	# plt.show()
	data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
	data = np.mean(data.reshape(fig.canvas.get_width_height()[::-1] + (3,)),axis =2)
	score = np.sum(np.abs(data-img))
	print i,score
	plt.cla()
	if score<bestScore:
		print 'a'
		bestScore = score
		bestData = data

plt.close()
plt.imshow(bestData,cmap='Greys_r')
# plt.set_aspect('equal')
plt.axis('off')
# plt.savefig('test.png')
plt.show()


# fig = plt.figure()
# # If we haven't already shown or saved the plot, then we need to
# # draw the figure first...
# fig.canvas.draw()

# # Now we can save it to a numpy array.
# data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
# data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))