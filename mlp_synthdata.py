import logging
import os

logging.basicConfig(level=logging.INFO)

from deepy.dataset import MiniBatches,BasicDataset
from deepy.networks import NeuralClassifier
from deepy.layers import Dense, Softmax
from deepy.trainers import MomentumTrainer, LearningRateAnnealer
from SynthDataset import SynthDataset

model_path = os.path.join(os.path.dirname(__file__), "models", "model_10000_op.gz")

if __name__ == '__main__':
    model = NeuralClassifier(input_dim=32*32)
    model.stack(Dense(400, 'tanh'),
                 Dense(100, 'tanh'),
                 Dense(3, 'linear'),
                 Softmax())

    #trainer = MomentumTrainer(model, {"weight_l2": 0.01})
    trainer = MomentumTrainer(model, {"learning_rate": LearningRateAnnealer.learning_rate(0.001)})
    

    annealer = LearningRateAnnealer(trainer)

    mlp_synthDataSet = MiniBatches(SynthDataset())

    trainer.run(mlp_synthDataSet, controllers=[annealer])

    model.save_params(model_path)
