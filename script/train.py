# -*- coding: utf-8 -*-

import sys, os
import pickle
import argparse
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from predlife import trainer

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True)
parser.add_argument('--output', required=True)
parser.add_argument('--N', required=True, type=int)
args = parser.parse_args()

def main():
    lines = open(args.dataset, 'r').readlines()
    dataset = []
    for i in range(0, len(lines), 3):
        input = [int(c) for c in lines[i].rstrip().split('\t')[1]]
        output = [int(c) for c in lines[i+1].rstrip().split('\t')[1]]
        dataset.append((input, output))
    trained_network = trainer.train(args.N, dataset)
    with open(args.output, 'w+') as f:
        pickle.dump(trained_network, f)

if __name__ == '__main__':
    main()
