# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from predlife.util import (convert_seed_to_life_list,
                           to_boolstring)

import argparse, random
from predlife.life import evolve

parser = argparse.ArgumentParser()
parser.add_argument('--N', default=100000, type=int)
parser.add_argument('--rule', default=30, type=int)
parser.add_argument('--size', default=20, type=int)
parser.add_argument('--max_generation', default=100, type=int)
parser.add_argument('--seed', default=100, type=int)
parser.add_argument('--output', required=True)
args = parser.parse_args()

def main():
    combination = 2 ** args.size
    if args.seed > combination:
        print 'seed should be less than %d' % combination
        exit()
    f = open(args.output, 'w+')
#    for i in range(args.seed, 2 ** args.size, 1):
    for i in range(args.N):
        sys.stdout.write("Progress: %d/%d \r" % (i, args.N))
        sys.stdout.flush()
        r = random.randint(0, 2 ** args.size)
        f.write('%d\t%s\n' % (0, to_boolstring(r, args.size)))
        life = evolve(args.max_generation,
                      args.rule,
                      r,
                      args.size)
        f.write('%d\t%s\n\n' % (args.max_generation, life))
    f.close()

if __name__ == '__main__':
    main()
