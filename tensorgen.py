from scipy import misc
import numpy as np
import os

# Get the maximum X/Y dimension for each image in this folder
def getMaxWidthHeight(fileName):
    imagearr = misc.imread(fileName)
    return imagearr.shape[0], imagearr.shape[1]

# read image pixels array
def populateImageTensor(fileName,imgNumber,tensorArray,w,h):
    imagearr = misc.imread(fileName)
    #normalizing the pixel values to be in the range of 0 to 1
    imagearr = imagearr/255.0
    imageWidth = imagearr.shape[0]
    imageHeight = imagearr.shape[1]
    #create a view of the tensor - its mostly like
    tensorView = tensorArr[imgNumber,:,0:imageWidth,0:imageHeight]
    imagearr = np.reshape(imagearr,(3,imageWidth,imageHeight))
    np.copyto(tensorView,imagearr)

# get path for images
currentPath = os.path.abspath(os.curdir)
filenames = next(os.walk(currentPath))[2]

imgCount = 0
processFiles = []
listofX = []
listofY = []

for file in filenames:
    fileName, fileExtension = os.path.splitext(file)
    if fileExtension == ".png":
        imgCount = imgCount + 1
        processFiles.append(file)
        x,y = getMaxWidthHeight(file)
        # get the max width, height
        listofX.append(x)
        listofY.append(y)

X = max(listofX)
Y = max(listofY)

# create 4-d array tensor
tensorArr = np.ndarray(shape=(10,3,X,Y),dtype='float64')
tensorArr.fill(-1)

i = 0
for file in processFiles:
    populateImageTensor(file,i,tensorArr, X, Y)
    i = i + 1
