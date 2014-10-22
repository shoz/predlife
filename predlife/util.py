# -*- coding: utf-8 -*-

import math

def to_boolstring(n, digits):
    return "{0:b}".format(n).zfill(digits)

def convert_seed_to_life_list(n, size):
    boolstring = to_boolstring(n, size)
    return [int(c) for c in boolstring]

def calc_match_ratio(life1, life2):
    if len(life1) != len(life2):
        return -1
    dist = 0
    for c1, c2 in zip(life1, life2):
        c1 = int(c1)
        c2 = int(c2)
        dist += math.sqrt((c1 - c2)**2)
    return 1.0 - dist/float(len(life1))

