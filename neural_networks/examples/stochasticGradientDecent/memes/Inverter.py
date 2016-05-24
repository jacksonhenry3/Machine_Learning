import sys
from os import walk
sys.path.insert(0, '../../../network')
from neuralNetwork import network

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

N = 35

path = './images/succesKid'
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

trainingData = []

for i,fileName in enumerate(f):
    img = Image.open(path+'/'+fileName)
    rsize = img.resize((N,N)) # Use Pillow to resize
    rsize = rsize.convert(mode = "L")
    rsizeArr = np.asarray(rsize).flatten()  # Get array back
    if rsizeArr.shape == (N*N,):
        trainingData.append((rsizeArr,[1]))

path = './images/FP'
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for i,fileName in enumerate(f):
    img = Image.open(path+'/'+fileName)
    rsize = img.resize((N,N)) # Use Pillow to resize
    rsize = rsize.convert(mode = "L")
    rsizeArr = np.asarray(rsize).flatten()  # Get array back
    if rsizeArr.shape == (N*N,):
        trainingData.append((rsizeArr,[0]))




#generate the network
meme_recogniser     = network([N*N,1000,1])

#give the network the training data
meme_recogniser.train(trainingData,errorThreshold = .04,eta = .2,verbose = True)

numberOfImages = len(trainingData)
numberOfCorrectGuesses = 0
for d in trainingData:
    inpt = d[0]
    otpt = d[1]
    guess = np.rint(meme_recogniser.feedForward(inpt)[-1])
    if guess == otpt:
        numberOfCorrectGuesses+=1.
print "test memes classified with "+str(numberOfCorrectGuesses/numberOfImages*100)+"% \acuracy"

testData = []
path = './images/test'
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for i,fileName in enumerate(f):
    img = Image.open(path+'/'+fileName)
    rsize = img.resize((N,N)) # Use Pillow to resize
    rsize = rsize.convert(mode = "L")
    rsizeArr = np.asarray(rsize).flatten()  # Get array back
    if rsizeArr.shape != (N*N):
        testData.append(rsizeArr)



ConfessionBearIndeces = []


for i,d in enumerate(testData):
    if d.shape == (N*N,):
        guess = meme_recogniser.feedForward(d)[-1]
        if guess >.999:
            print guess
            ConfessionBearIndeces.append(i)
ConfessionBears = []
for i,fileName in enumerate(f):
    if i in ConfessionBearIndeces:
        img = Image.open(path+'/'+fileName)
        ConfessionBears.append(img)

for bear in ConfessionBears:
    plt.imshow(bear)
    plt.show()
