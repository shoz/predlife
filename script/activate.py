# -*- coding: utf-8 -*-

import argparse
import pickle
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from predlife.util import convert_seed_to_life_list 

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True)
parser.add_argument('--seed', required=True, type=int)
parser.add_argument('--size', required=True, type=int)
args = parser.parse_args()

def main():
    with open(args.path, 'r') as f:
        nn = pickle.loads(f)
    input = convert_seed_to_life_list(args.seed, args.size)
    nn.activate()

if __name__ == '__main__':
    main()
