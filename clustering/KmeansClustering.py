import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


   # 1. sepal length in cm
   # 2. sepal width in cm
   # 3. petal length in cm
   # 4. petal width in cm
TrainingData = np.loadtxt("./Data2",delimiter = ',',skiprows  = 1,dtype = str)
nFeatures = TrainingData.shape[1]-1
data = TrainingData[:,0:nFeatures].astype(float)

k=2


dataRanges = []
startingPnts = []
clusters = []
for i in range(nFeatures):
	mn = np.min(data[:,i].astype(float))
	mx = np.min(data[:,i].astype(float))
	dataRanges.append([mn,mx])
for i in range(k):
	pnt = np.random.random(nFeatures)
	clusters.append([])
	startingPnts.append(pnt)

for pnt in data:
	minDist = 10
	for i,centroid in enumerate(startingPnts):
		distance = np.linalg.norm(pnt-centroid)
		if distance<minDist:
			minDist = distance
			clusters[i].append(pnt)

for centroid in  enumerate(startingPnts):
	print np.mean(clusters[i])
	print clusters[i]
	centroid = np.mean(clusters[i])
	


# detectClusters(TrainingData,2)
