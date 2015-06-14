import os
import numpy as np
from scipy import misc
from datagen import get_samples
from deepy.dataset import Dataset

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

class SynthDataset(Dataset):

    def __init__(self):
        self._target_size = 3
        self._train_set = get_synthetic_data(8000)
        self._valid_set = get_synthetic_data(2000)
        self._test_set = get_synthetic_data(1000)

    def train_set(self):
        return self._test_set

    def valid_set(self):
        return self._test_set

    def test_set(self):
        return self._test_set
