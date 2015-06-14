import os
import numpy as np
from scipy import misc
from datagen import get_samples
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
        gs = np.reshape(grayscaled,(1024))
        grayscales.append( (gs,label) )
    return np.array(grayscales)
