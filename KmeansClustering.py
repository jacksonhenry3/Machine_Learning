import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


   # 1. sepal length in cm
   # 2. sepal width in cm
   # 3. petal length in cm
   # 4. petal width in cm
TrainingData = np.loadtxt("./Data2",delimiter = ',',skiprows  = 1,dtype = str)

def detectClusters(data,k):
	dimensionality = data.shape[1]-1
	dataRanges = []
	startingPnts = []
	for i in range(dimensionality):
		mn = np.min(data[:,i].astype(float))
		mx = np.min(data[:,i].astype(float))
		dataRanges.append([mn,mx])
	for i in range(k):
		pnt = np.random.random(dimensionality)
		startingPnts.append(pnt)


detectClusters(TrainingData,2)
