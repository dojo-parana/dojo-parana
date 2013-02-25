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
    return total

class hpTest(unittest.TestCase):
    def test_um(self):
        self.assertEqual(PrecoLivro, calcula([1]))

    def test_dois(self):
        self.assertEqual((PrecoLivro*2)*0.95, calcula([2]))

    def test_um_um(self):
        self.assertEqual((PrecoLivro*2), calcula([1,1]))

    def test_dois_um(self):
        self.assertEqual(42 + 79.8, calcula([2,1]))

    def test_dois_dois(self):
        self.assertEqual(79.8+ 79.8, calcula([2,2]))

    def test_um_dois_um(self):
        self.assertEqual(PrecoLivro + 79.8 + PrecoLivro, calcula([1,2,1]))
    
			
if __name__ == '__main__':
    unittest.main()
