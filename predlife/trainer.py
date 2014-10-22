# -*- coding: utf-8 -*-

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.structure import TanhLayer
from pybrain.tools.shortcuts import buildNetwork

def train(dataset):
    ds = SupervisedDataSet(20, 20)
    for data in dataset:
        ds.addSample(data[0], data[1])
    net = buildNetwork(20, 30, 10, 20, bias=True, hiddenclass=TanhLayer)
    trainer = BackpropTrainer(net, ds)
    trainer.train()
    return trainer
