# -*- coding: utf-8 -*-

import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--N', default=1, required=True, type=int)
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

def main():
    with open(args.input, 'r') as f:
        nn = pickle.load(f)
    for i in range(args.N):
        nn.train()
    with open(args.output, 'w+') as f:
        pickle.dump(nn, f)

if __name__ == '__main__':
    main()
