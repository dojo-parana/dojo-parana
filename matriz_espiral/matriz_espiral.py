#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2011-08-24 19:13:39
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class matriz_espiral:
    def __init__(self, colunas, linhas):
        self.colunas=colunas
        self.linhas=linhas
        self.matriz = [
            [0,0,0],
            0,
            0,
            0
        ]

    

class matriz_espiralTest(unittest.TestCase):
    def test_init(self):
        self.assertNotEqual(matriz_espiral(3,4), None)

    def test_linhas_colunas_da_matriz(self):
        matriz = matriz_espiral(3,4)
        self.assertEqual(matriz.colunas,3)
        self.assertEqual(matriz.linhas,4)
    
    def test_cria_matriz(self):
        matriz = matriz_espiral(3,4)
        self.assertEquals(4, len(matriz.matriz))
        self.assertEquals(3, len(matriz.matriz[0]))

        
if __name__ == '__main__':
    unittest.main()
