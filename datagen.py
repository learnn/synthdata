from PIL import Image, ImageFont, ImageDraw
import random
import os
import numpy as np
from scipy import misc

def drawRect(index):
    im = Image.new('RGB', (32,32), (255,255,255))
    dr = ImageDraw.Draw(im)
    width = random.randint(5, 28)
    height = random.randint(5, 28)
    size = (width,height)
    x = random.randint(0,32-width)
    y = random.randint(0, 32-height)
    position = (x,y)
    fillColor = "rgb({0},{1},{2})".format(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    dr.rectangle((position,size), fill=fillColor)
    #return im.save("rectangle_{0}.png".format(index))
    return im

def drawTriangle(index):
    im = Image.new('RGB', (32,32), (255,255,255))
    dr = ImageDraw.Draw(im)
    x1 = random.randint(0,28)
    y1 = random.randint(0, 28)
    x2 = random.randint(0,28)
    y2 = random.randint(0, 28)
    x3 = random.randint(0,28)
    y3 = random.randint(0, 28)
    position = (x1,y1,x2,y2,x3,y3)
    fillColor = "rgb({0},{1},{2})".format(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    dr.polygon(position, fill=fillColor)
    #return im.save("triangle_{0}.png".format(index))
    return im

def drawCircle(index):
    im = Image.new('RGB', (32,32), (255,255,255))
    dr = ImageDraw.Draw(im)
    width = random.randint(5, 28)
    height = random.randint(5, 28)
    x = random.randint(0,32-width)
    y = random.randint(0, 32-height)
    bounds = (x,y,width,height)
    fillColor = "rgb({0},{1},{2})".format(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    dr.ellipse(bounds, fill=fillColor)
    #return im.save("circle_{0}.png".format(index))
    return im

options = {
    0 : drawRect,
    1 : drawTriangle,
    2 : drawCircle
}

def get_synthetic_data(samples=1000):
    imagesamples = get_samples(samples)
    return get_grayscale_tensor(imagesamples)


def get_grayscale_tensor(samples):
    i = 0
    grayscales = []
    for sample in samples:
        current_image,label = sample
        current_image = misc.fromimage(current_image)/255.0
        grayscaled = np.dot(current_image[...,:3], [0.299, 0.587, 0.144])
        gs = np.reshape(grayscaled,(1024)).tolist()
        grayscales.append( (gs,label) )
    return grayscales

def get_samples(samples=1000):
    shapes = []
    for i in range(samples):
        choice = random.randint(0,2)
        shapes.append((options[choice](i),choice))
    return shapes
