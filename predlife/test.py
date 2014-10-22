# -*- coding: utf-8 -*-

from predlife.life import make_wolfram_rule

def test_wolfram_rule():
    rule30 = {'111': False, '110': False, '101': False, '100': True,
              '011': True, '010': True, '001': True, '000': False}
    assert make_wolfram_rule(30) == rule30

