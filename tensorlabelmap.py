import os
import numpy

label  = -1

# get path for images
currentPath = os.path.abspath(os.curdir)
filenames = next(os.walk(currentPath))[2]

labels = []

for file in filenames:
    fileName, fileExtension = os.path.splitext(file)
    if fileExtension == ".png":
        imgShape = fileName.split("_")[0]
        if imgShape == "rectangle":
            label = 0 
        elif imgShape == "circle":
            label = 1
        elif imgShape == "triangle":
            label = 2
        labels.append(label)
        
labelTensorSize = len(labels)
tensorArr = numpy.zeros(shape=(labelTensorSize))

i = 0
for label in labels:
    tensorArr[i] = int(label)
    i = i + 1

print tensorArr