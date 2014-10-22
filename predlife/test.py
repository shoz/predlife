# -*- coding: utf-8 -*-

from predlife.life import make_wolfram_rule
from predlife.util import *

def test_wolfram_rule():
    rule30 = {'111': False, '110': False, '101': False, '100': True,
              '011': True, '010': True, '001': True, '000': False}
    assert make_wolfram_rule(30) == rule30

def test_calc_match_ratio():
    assert calc_match_ratio('111', '111') == 1.0
    assert calc_match_ratio('111', '000') == 0.0
    assert calc_match_ratio('1111', '1100') == 0.5
