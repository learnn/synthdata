import os
import numpy as np

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
            label = [1,0,0]
        elif imgShape == "circle":
            label = [0,1,0]
        elif imgShape == "triangle":
            label = [0,0,1]
        labels.append(label)

tensorArr = np.array(labels)
