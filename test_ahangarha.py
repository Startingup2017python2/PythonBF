# -*- coding: utf-8 -*-
"""
testunit written for my second homework for StartingUp2017 Project

@author: sama
"""

import unittest
import ahangarha

class TestAhangarha(unittest.TestCase):
    
    def test_inc(self):
        code = "+"*65 + "."
        result = ahangarha.execute(code)
        self.assertEqual(result, 'A')

    def test_dec(self):
        code = "+"*66 + '-.'
        result = ahangarha.execute(code)
        self.assertEqual(result, 'A')
    
    def test_shift_right(self):
        code = "+"*65 + '.>' + '+'*65 + '.'
        result = ahangarha.execute(code)
        self.assertEqual(result, 'AA')
    
    def test_shift_right_left(self):
        code = "+"*64 + '>' + '+'*65 + '<+.>.'
        result = ahangarha.execute(code)
        self.assertEqual(result, 'AA')
    
    def test_simple_loop(self):
        code = '++++++++[>++++++++<-]>+.'
        result = ahangarha.execute(code)
        self.assertEqual(result, 'A')
        

if __name__ == '__main__':
    unittest.main()