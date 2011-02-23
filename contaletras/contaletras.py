# -*- coding:utf-8 -*-

'''
Se os números de 1 a 5 fossem escritos em palavras: um, dois, três, quatro, cinco, então teríamos utilizado 2 + 4 + 4 + 6 + 5 = 21 letras no total.
Se todos os números de 1 até 1000 fossem escritos em palavras, quantas letras nós teríamos utilizado?
'''

import unittest

class ContaLetras:
    def int_2_palavra(self, numero):

        dicionario = {
            1: 'um',
            2: 'dois',
            3: 'tres',
            4: 'quatro',
            5: 'cinco',
            6: 'seis',
            7: 'sete',
            8: 'oito',
            9: 'nove',        
        }
        
        return dicionario[numero]

class ContaLetrasTest(unittest.TestCase):
    def test_int_1_para_palavra(self):      
        self.assertEqual(ContaLetras().int_2_palavra(1), 'um')
    
    def test_int_2_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(2), 'dois')
        
    def test_int_3_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(3), 'tres')
        
    def test_int_4_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(4), 'quatro')
        
    def test_int_5_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(5), 'cinco')
        
    def test_int_6_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(6), 'seis')
        
    def test_int_7_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(7), 'sete')

    def test_int_8_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(8), 'oito')
        
    def test_int_9_para_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(9), 'nove')
        

if __name__ == '__main__':
    unittest.main()    
