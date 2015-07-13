import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


   # 1. sepal length in cm
   # 2. sepal width in cm
   # 3. petal length in cm
   # 4. petal width in cm
TrainingData = np.loadtxt("Data2",delimiter = ',',skiprows  = 1,dtype = str)


class Knn(object):
	"""docstring for data"""
	def __init__(self, TrainingData):
		self.TrainingData = TrainingData


		self.nFeatures = self.TrainingData.shape[1]-1
		self.data = TrainingData[:,0:self.nFeatures].astype(float)
		self.FeatureRange = []

		self.normalize()
	def normalize(self,weights = None):
		if weights == None:
			weights = np.ones(self.nFeatures)
		for i in range(self.nFeatures):

			mn = np.min(self.data[:,i])
			self.data[:,i] -= mn
			mx = np.max(self.data[:,i])
			self.data[:,i] /= mx

			self.FeatureRange.append([mn,mx])
	def Check(self,pnt):
		for i in range(self.nFeatures):
			pnt[i] -= self.FeatureRange[i][0]
			pnt[i] /= self.FeatureRange[i][1]

		distances = []
		for i in range(len(self.data)):
			dist = np.linalg.norm(pnt-self.data[i])
			distances.append(dist)
		order = np.argsort(distances)
		c = Counter(self.TrainingData[:,self.nFeatures][order][0:7])
		ans = c.most_common(3)
		print(ans[0][0])





boop = Knn(TrainingData)

pnt = np.array([7.0,3.2,4.7,1.85])
boop.Check(pnt)
