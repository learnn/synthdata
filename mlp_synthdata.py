import logging
import os

logging.basicConfig(level=logging.INFO)

from deepy.dataset import MiniBatches,BasicDataset
from deepy.networks import NeuralClassifier
from deepy.layers import Dense, Softmax
from deepy.trainers import MomentumTrainer, LearningRateAnnealer
from SynthDataset import SynthDataset

if __name__ == '__main__':
    model = NeuralClassifier(input_dim=32*32)
    model.stack(Dense(100, 'tanh'),
                 Dense(100, 'tanh'),
                 Dense(3, 'linear'),
                 Softmax())

    trainer = MomentumTrainer(model, {"weight_l2": 0.001})

    annealer = LearningRateAnnealer(trainer)

    mlp_synthDataSet = MiniBatches(SynthDataset())

    trainer.run(mlp_synthDataSet, controllers=[annealer])

    #model.save_params(default_model)
