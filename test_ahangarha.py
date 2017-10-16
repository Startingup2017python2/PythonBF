# -*- coding: utf-8 -*-
"""
testunit written for my second homework for StartingUp2017 Project

@author: sama
"""

import unittest
import ahangarha

class TestAhangarha(unittest.TestCase):
    
    def test_operations(self):
        code = "+"*65 + "."
        self.assertEqual(ahangarha.execute(code), 'A')

        code = "+"*66 + '-.'
        self.assertEqual(ahangarha.execute(code), 'A')
    
        code = "+"*65 + '.>' + '+'*65 + '.'
        self.assertEqual(ahangarha.execute(code), 'AA')
    
        code = "+"*64 + '>' + '+'*65 + '<+.>.'
        self.assertEqual(ahangarha.execute(code), 'AA')

        code = '++++++++[>++++++++<-]>+.'
        self.assertEqual(ahangarha.execute(code), 'A')
    
    def test_abnormal_input(self):
        code = 'blah' + '+'*65 + '.' + 'blah'
        self.assertEqual(ahangarha.execute(code), 'A')
        
        code = ''
        self.assertRaises(ValueError, ahangarha.execute, code)
        
        code = 'blah'
        self.assertRaises(ValueError, ahangarha.execute, code)

if __name__ == '__main__':
    unittest.main()