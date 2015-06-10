from PIL import Image, ImageFont, ImageDraw
import random

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
    return im.save("rectangle_{0}.png".format(index))

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
    return im.save("triangle_{0}.png".format(index))

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
    return im.save("circle_{0}.png".format(index))

options = {
    0 : drawRect,
    1 : drawTriangle,
    2 : drawCircle
}

max = 10;

for i in range(max):
    choice = random.randint(0,2)
    options[choice](i)
