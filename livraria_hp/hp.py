#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2013-02-25 19:41:35
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

PrecoLivro = 42
QuantidadeMaximaDesconto = 6

def calcula(lista):
    total = 0
    progressao = 0.05

    for qtde in lista:
        if qtde < QuantidadeMaximaDesconto:
            desconto = progressao * (qtde - 1)
        else:
            desconto = 0.0
        total += qtde * PrecoLivro * (1 - desconto)
    return total

class calculoDescontoProgressivoTest(unittest.TestCase):
    def test_uma_copia(self):
        self.assertEqual(42, calcula([1]))

    def test_duas_copias(self):
        self.assertEqual(79.8, calcula([2]))

    def test_duas_copias_distintas(self):
        self.assertEqual(84, calcula([1,1]))

    def test_duas_copias_mais_uma_distinta(self):
        self.assertEqual(121.8, calcula([2,1]))

    def test_duas_copias_mais_duas(self):
        self.assertEqual(159.6, calcula([2,2]))

    def test_uma_copia_mais_duas_mais_uma(self):
        self.assertEqual(163.8, calcula([1,2,1]))
    
    def test_tres_copias(self):
        self.assertEqual(113.4, calcula([3]))
	
    def test_quatro_copias(self):
        self.assertAlmostEqual(142.8, calcula([4]))

    def test_cinco_copias(self):
        self.assertEqual(168, calcula([5]))
    
    def test_seis_copias(self):
        self.assertEqual(6 * 42, calcula([6]))
		
if __name__ == '__main__':
    unittest.main()	
