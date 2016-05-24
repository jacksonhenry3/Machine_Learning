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
img = scipy.misc.imresize(img,100)
img = np.mean(img[:,:,0:3],axis = 2)

width = img.shape[1]
height = img.shape[0]

# plt.imshow(img,cmap='Greys_r')
# # plt.show()

# width = img.shape[1]
# height = img.shape[0]
# div = 1

# def getImgAverageOverLine(imgData,x1,x2,y1,y2):

# 	if x2==x1:
# 		return(255)
# 	slope = (y2-y1)/(x2-x1)
# 	# print slope
# 	x = np.linspace(x1,x2,height)
# 	y = np.clip((slope*(x-x1)+y1).astype(int),0,width-1)
# 	x = np.floor(x).astype(int)

# 	return(np.mean(imgData[x,y]))

def generateLine(x1,x2,y1,y2):
	template = np.zeros((height,width))

	if x2==x1:
		return(template)
	slope = (y2-y1)/(x2-x1)
	# print slope
	x = np.linspace(x1,x2,width)
	y = np.clip((slope*(x-x1)+y1).astype(int),0,height-1)
	x = np.clip(np.floor(x).astype(int),0,width-1)
	template[y,x] = 255
	return(template)


# plt.imshow(A)
# plt.show()
N = 2
numComps = 0

guess = np.ones((height,width))*255

for row1 in np.arange(0,width,width/N):
	print row1/float(width)
	for col1 in np.arange(0,height,height/N):
		for row2 in np.arange(0,width,width/N):
			for col2 in np.arange(0,height,height/N):
				# if not ((row1 == row2 and col2<col1) or (row1<row2)):
				numComps+=1
				B = np.zeros((height,width))
				B[col2-5:col2+5,row2-5:row2+5] = 255
				A = generateLine(col1,col2,row1,row2)
				# if np.mean(np.square(img-(guess-A)))<np.mean(np.square(img-(guess))):
				# print np.mean(guess)
				guess = guess-A
				guess = guess-B
				# print np.mean(guess)

				# if (col2-col1)**2+(row2-row1)**2<900:
				# if getImgAverageOverLine(img,row1,row2,col1,col2)<255/2.:
				# 	plt.plot([col1,col2],[row1,row2],'k',linewidth=.2)

# (y1,x1),(y2,x2)
# print numComps
# print np.mean(guess)
# print np.max(np.clip(guess,0,255))
# guess = guess - np.min(guess)
# A = generateLine(1,20,1,20)
# print A
guess = np.clip(guess,0,255)
plt.imshow(guess,cmap='Greys_r',interpolation = 'none')
plt.show()

# # for i in range(0,height,div):
# # 	for j in range(0,width,div):
# # 		if np.mean(img[i,j:j+div]) < 255/2.:
# # 			plt.plot([j,j+div],[i,i],'k')

# # for i in range(0,height,div):
# # 	for j in range(0,width,div):
# # 		if np.mean(img[i:i+div,j]) < 255/2.:
# # 			plt.plot([j,j],[i,i+div],'k')

# # plt.show()
