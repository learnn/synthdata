import logging
import os

logging.basicConfig(level=logging.INFO)

from deepy.dataset import SynthDataset, MiniBatches
from deepy.networks import NeuralClassifier
from deepy.layers import Dense, Softmax
from deepy.trainers import MomentumTrainer, LearningRateAnnealer

default_model = os.path.join(os.path.dirname(__file__), "models", "mlp_synthdata.gz")

if __name__ == '__main__':
   model = NeuralClassifier(input_dim=32*32)
     model.stack(Dense(1024, 'relu'),
                 Dense(500, 'relu'),
                 Dense(3, 'linear'),
                 Softmax())

    trainer = MomentumTrainer(model, {"weight_l2": 0.001})

    annealer = LearningRateAnnealer(trainer)

    mlp_synthDataSet = MiniBatches(SynthDataset(), batch_size=20)

    trainer.run(mlp_synthDataSet, controllers=[annealer])

    model.save_params(default_model)