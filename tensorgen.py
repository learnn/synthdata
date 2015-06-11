from scipy import misc
import numpy
import os

# Get the maximum X/Y dimension for each image in this folder
def getMaxWidthHeight(fileName):
    imagearr = misc.imread(fileName)
    return imagearr.shape[0], imagearr.shape[1]
    
# read image pixels array
def populateImageTensor(fileName,imgNumber,tensorArray,w,h):
    imagearr = misc.imread(fileName)
    for i in range(w):
        for j in range(h):
            for k in range(3):
                pixel = imagearr[i][j][k]
                if pixel < 255:
                    tensorArray[imgNumber][k][i][j] = pixel
                else:
                    tensorArray[imgNumber][k][i][j] = -1

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
tensorArr = numpy.zeros(shape=(10,3,X,Y))
      
i = 0
for file in processFiles:
    populateImageTensor(file,i,tensorArr, X, Y)
    i = i + 1
    
print tensorArr