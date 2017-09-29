#!/usr/bin/env python3

import unittest

def traduz(palavra):
    if palavra[0] == 'A':
        return '2'
    elif palavra[0] == 'D':
        return '3'
    elif palavra[0] == 'G':
        return '4'
    else:
        return '5'

class TestCelular(unittest.TestCase):
    def test_A_deve_retornar_2(self):
        esperado = '2'
        
        self.assertEqual(traduz('A'), esperado)
       
    def test_D_deve_retornar_3(self):
        esperado = '3'
        
        self.assertEqual(traduz('D'), esperado)
       
    def test_G_deve_retornar_4(self):
        esperado = '4'
        
        self.assertEqual(traduz('G'), esperado)
    
    def test_J_deve_retornar_5(self):
        esperado = '5'
        
        self.assertEqual(traduz('J'), esperado)

if __name__ == '__main__':
    unittest.main()
