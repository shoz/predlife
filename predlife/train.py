# -*- coding: utf-8 -*-

from pybrain.supervised.trainers import BackpropTrainer

def train():
    ds = SupervisedDataSet(20, 20)
    
    net = buildNetwork(20, 30, 10, 20, bias=True, hiddenclass=TanhLayer)
    trainer = BackpropTrainer(net, ds)
    
if __name__ == '__main__':
    main()
