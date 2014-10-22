# -*- coding: utf-8 -*-

def to_boolstring(n, digits):
    return "{0:b}".format(n).zfill(digits)

def convert_seed_to_life_list(n, size):
    boolstring = to_boolstring(n, size)
    return [int(c) for c in boolstring]
