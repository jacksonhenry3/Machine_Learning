import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import time
# np.random.seed(0)

   # 1. sepal length in cm
   # 2. sepal width in cm
   # 3. petal length in cm
   # 4. petal width in cm
TrainingData = np.loadtxt("./Data2",delimiter = ',',skiprows  = 1,dtype = str)
nFeatures = TrainingData.shape[1]-1
data = TrainingData[:,0:nFeatures].astype(float)

numClusters  = 3
dataMins   = []
dataMaxs   = []
startingPnts = []
clusters     = [[] for i in range(numClusters)]

for i in range(nFeatures):
	mn = np.min(data[:,i].astype(float))
	mx = np.max(data[:,i].astype(float))
	dataMins.append(mn)
	dataMaxs.append(mx)

dataMins = np.array([dataMins,]*numClusters)
dataMaxs = np.array([dataMaxs,]*numClusters)


startingPnts = np.random.random((numClusters,nFeatures))


dataMins*=np.ones((numClusters,nFeatures))
dataMaxs*=np.ones((numClusters,nFeatures))
startingPnts+=dataMins/dataMaxs
startingPnts*=dataMaxs/(1+dataMins/dataMaxs)




for i in range(10):
	clusters     = [[] for kappa in range(numClusters)]
	for pnt in data:
		distance = []
		for idx,centroid in enumerate(startingPnts):

			distance.append(np.linalg.norm(pnt-centroid))
		idx = np.argmin(distance)
		clusters[idx].append(pnt)

	for j,centroid in enumerate(startingPnts):
		startingPnts[j] = np.mean(clusters[j],0)
	print 'Done with '+str(i)+' iterations'

	for i in range(numClusters):
		for pnt in clusters[i]:
			x = [pnt[0],startingPnts[i][0]]
			y = [pnt[1],startingPnts[i][1]]
			plt.plot(x,y,'k')

	plt.plot(data[:,0],data[:,1],'.')
	plt.plot(startingPnts[:,0],startingPnts[:,1],'r*')
	# plt.show()
	plt.savefig('test.png')
	plt.close()




for i in range(numClusters):
	for pnt in clusters[i]:
		x = [pnt[3],startingPnts[i][3]]
		y = [pnt[1],startingPnts[i][1]]
		plt.plot(x,y,'k')

plt.plot(data[:,3],data[:,1],'.')
plt.plot(startingPnts[:,3],startingPnts[:,1],'r*')
plt.show()
plt.savefig('test.png')
plt.close()




# detectClusters(TrainingData,2)
