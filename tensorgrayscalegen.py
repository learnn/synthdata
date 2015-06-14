from scipy import misc
import numpy as np
import os

# Get the maximum X/Y dimension for each image in this folder
def getMaxWidthHeight(fileName):
    imagearr = misc.imread(fileName)
    return imagearr.shape[0], imagearr.shape[1]

# Read image pixels array
def populateGreyScaleImageTensor(fileName,imgNumber,tensorArray,w,h):
    imagearr = misc.imread(fileName)
    #normalizing the pixel values to be in the range of 0 to 1
    imagearr = imagearr/255.0
    imageWidth = imagearr.shape[0]
    imageHeight = imagearr.shape[1]
    
    # Get grayscale from image
    print imagearr[...,:3]
    b = np.dot(imagearr[...,:3], [0.299, 0.587, 0.144])
    #create a view of the tensor - a pointer to the 3d array within the 4d array.
    #tensorView = tensorArray[imgNumber,0:imageWidth]
    #imagearr = np.reshape(imagearr,(3,imageWidth,imageHeight))
    #print imagearr
    #np.copyto(tensorView,imagearr)
    print b

# Get path for images
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

print X, Y

# create 2-d tensor tuple
greyScaleTensor = np.ndarray(shape=(10,X*Y),dtype='float64')
greyScaleTensor.fill(-1)

i = 0
for file in processFiles:
    populateGreyScaleImageTensor(file,i,greyScaleTensor, X, Y)
    i = i + 1