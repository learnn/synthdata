import os
import numpy as np
from scipy import misc
from datagen import get_synthetic_data
from deepy.dataset import Dataset
import cPickle as pickle
import gzip

class SynthDataset(Dataset):

    def __init__(self):
        self._target_size = 3
        self._train_set, self._valid_set, self._test_set = pickle.load(gzip.open("synth_10000.pkl.gz", 'rb'))

    def train_set(self):
        return self._test_set

    def valid_set(self):
        return self._test_set

    def test_set(self):
        return self._test_set
