import os
import numpy as np
from scipy import misc
from datagen import get_synthetic_data
import cPickle as pickle
import gzip

train_set = get_synthetic_data(samples=8000)
valid_set = get_synthetic_data(samples=2000)
test_set = get_synthetic_data(samples=1000)

data = (train_set,valid_set,test_set)

f = gzip.open('synth_10000.pkl.gz','wb')
pickle.dump(data,f)
f.close()
