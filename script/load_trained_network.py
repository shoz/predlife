# -*- coding: utf-8 -*-

import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True)
args = parser.parse_args()

def main():
    with open(args.path, 'r') as f:
        nn = pickle.loads(f)
    nn.activate()

if __name__ == '__main__':
    main()
