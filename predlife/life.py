# -*- coding: utf-8 -*-

import sys
import argparse
import random
from predlife.util import to_boolstring

def make_wolfram_rule(rule):
    patterns = ['111', '110', '101', '100',
                '011', '010', '001', '000']
    bitrule = to_boolstring(rule, 8)
    ret = {}
    for pattern, bit in zip(patterns, bitrule):
        ret[pattern] = bool(int(bit))
    return ret

def evolve_once(life, pattern):
    ret = ''
    _life = life + life[0]
    for i in range(len(life)):
        neighbors = life[i-1] + life[i] + _life[i+1]
        token = str(int(pattern[neighbors]))
        ret += token
    return ret

def evolve(generation, rule, seed, size):
    pattern = make_wolfram_rule(rule)
    life = to_boolstring(seed, size)
    for gen in range(generation):
        life = evolve_once(life, pattern)
    return life

