from scipy import misc
import numpy

# read image pixels array
imagearr = misc.imread('circle_9.png')
print imagearr.shape

# create 4-d array tensor
a = numpy.zeros(shape=(10,3,32,32))
print a.shape

for i in range(32):
    for j in range(32):
        for k in range(3):
            pixel = imagearr[i][j][k]
            if pixel < 255:
                #print str(pixel) + " " + str(i) + " " + str(j) + " " + str(k)
                a[0][k][i][j] = pixel
            else:
                a[0][k][i][j] = -1
   
 #verify if we are correct, get co-ords by uncommenting pixel print above     
print a[0][0][15][13]
print a[0][1][15][13]
print a[0][2][15][13]