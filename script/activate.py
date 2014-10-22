# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import argparse
import pickle

from predlife.util import convert_seed_to_life_list 

parser = argparse.ArgumentParser()
parser.add_argument('--nn', required=True)
parser.add_argument('--seed', required=True, type=int)
parser.add_argument('--size', required=True, type=int)
args = parser.parse_args()

def main():
    with open(args.nn, 'r') as f:
        nn = pickle.load(f)
    input = convert_seed_to_life_list(args.seed, args.size)
    print nn.activate(input)

if __name__ == '__main__':
    main()
