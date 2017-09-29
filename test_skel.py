#!/usr/bin/env python3

import unittest

def traduz(palavra):
    dicionario_saida = {'A':'2','B':'22'} 

    for n in palavra:       
        if(n == 'A' or n == 'B'):
            return dicionario_saida[n]

        elif n == 'C':
            return '222'
        elif n == 'D':
            return '3'
        elif n == 'E':
            return '33'
        elif n == 'F':
            return '333'
        elif n == 'G':
            return '4'
        elif n == 'H':
            return '44'
        
        else:
            return '5'

class TestCelular(unittest.TestCase):
    def test_A_deve_retornar_2(self):
        esperado = '2'
        
        self.assertEqual(traduz('A'), esperado)
    
    def test_B_deve_retornar_22(self):
        esperado = '22'
        
        self.assertEqual(traduz('B'), esperado)
    
    def test_C_deve_retornar_222(self):
        esperado = '222'
        
        self.assertEqual(traduz('C'), esperado)
       
    def test_D_deve_retornar_3(self):
        esperado = '3'
        
        self.assertEqual(traduz('D'), esperado)
       
    def test_E_deve_retornar_33(self):
        esperado = '33'
        
        self.assertEqual(traduz('E'), esperado)

    def test_F_deve_retornar_333(self):
        esperado = '333'
        
        self.assertEqual(traduz('F'), esperado)

        
    def test_G_deve_retornar_4(self):
        esperado = '4'
        
        self.assertEqual(traduz('G'), esperado)

    def test_H_deve_retornar_44(self):
        esperado = '44'
        
        self.assertEqual(traduz('H'), esperado)
    

    def test_J_deve_retornar_5(self):
        esperado = '5'
        
        self.assertEqual(traduz('J'), esperado)
    

if __name__ == '__main__':
    unittest.main()
