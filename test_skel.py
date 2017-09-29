#!/usr/bin/env python3

import unittest

def traduz(palavra):
    if palavra[0] == 'A':
        return '2'
    else:
        return '3'

class TestCelular(unittest.TestCase):
    def test_A_deve_retornar_2(self):
        esperado = '2'
        
        self.assertEqual(traduz('A'), esperado)
       
    def test_D_deve_retornar_3(self):
        esperado = '3'
        
        self.assertEqual(traduz('D'), esperado)
       

if __name__ == '__main__':
    unittest.main()
