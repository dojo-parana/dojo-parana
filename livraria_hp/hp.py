#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2013-02-25 19:41:35
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

PrecoLivro = 42

def calcula(lista):
    total = 0

    for qtde in lista:
        if qtde == 1:
            total += PrecoLivro
        elif qtde == 2:
            total += PrecoLivro * 2 * 0.95
        elif qtde == 3:
            total += PrecoLivro * 3 * 0.9
        elif qtde == 4:
            total += PrecoLivro * 4 * 0.85
        elif qtde == 5:
            total += PrecoLivro * 5 * 0.80

    return total

class calculoDescontoProgressivoTest(unittest.TestCase):
    def test_uma_copia(self):
        self.assertEqual(PrecoLivro, calcula([1]))

    def test_duas_copias(self):
        self.assertEqual((PrecoLivro*2)*0.95, calcula([2]))

    def test_duas_copias_distintas(self):
        self.assertEqual((PrecoLivro*2), calcula([1,1]))

    def test_duas_copias_mais_uma_distinta(self):
        self.assertEqual(42 + 79.8, calcula([2,1]))

    def test_duas_copias_mais_duas(self):
        self.assertEqual(79.8+ 79.8, calcula([2,2]))

    def test_uma_copia_mais_duas_mais_uma(self):
        self.assertEqual(PrecoLivro + 79.8 + PrecoLivro, calcula([1,2,1]))
    
    def test_tres_copias(self):
        self.assertEqual(113.4, calcula([3]))
	
    def test_quatro_copias(self):
        self.assertAlmostEqual(142.8, calcula([4]))

    def test_cinco_copias(self):
        self.assertEqual(168, calcula([5]))

		
if __name__ == '__main__':
    unittest.main()	
