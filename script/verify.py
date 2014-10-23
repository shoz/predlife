# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import argparse
import pickle
import random

from predlife.util import *
from predlife.life import evolve

parser = argparse.ArgumentParser()
parser.add_argument('--nn', required=True)
parser.add_argument('--generation', required=True, type=int)
parser.add_argument('--rule', required=True, type=int)
#parser.add_argument('--seed', required=True, type=int)
parser.add_argument('--size', required=True, type=int)
parser.add_argument('--N', required=True, type=int)
args = parser.parse_args()

def main():
    with open(args.nn, 'r') as f:
        nn = pickle.load(f)
    ret = 0
    for i in range(args.N):
        r = random.randint(0, 2 ** args.size)
        input = convert_seed_to_life_list(r, args.size)
        predicted = nn.activate(input)
        bool_predicted = convert_float_to_boolstring(predicted)
        answer = evolve(args.generation, args.rule, r, args.size)
        ratio = calc_match_ratio(predicted, answer)
        ret += ratio
        print predicted
        print bool_predicted
        print answer
        print 
    print ret / float(args.N)

if __name__ == '__main__':
    main()
