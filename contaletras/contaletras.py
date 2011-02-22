# -*- coding:utf-8 -*-

'''
Se os números de 1 a 5 fossem escritos em palavras: um, dois, três, quatro, cinco, então teríamos utilizado 2 + 4 + 4 + 6 + 5 = 21 letras no total.
Se todos os números de 1 até 1000 fossem escritos em palavras, quantas letras nós teríamos utilizado?
'''

import unittest

class ContaLetras:
    def int_2_palavra(self, numero):
        return 'um'

class ContaLetrasTest(unittest.TestCase):
    def test_int_2_palavra(self):
        self.assertEqual(ContaLetras().int_2_palavra(1), 'um')

if __name__ == '__main__':
    unittest.main()    
