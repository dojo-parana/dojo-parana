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
        self.matriz = []
        for i in range(linhas):
            self.matriz.append([])
            for j in range(colunas):
                self.matriz[i].append(j+1+i)


                 
        

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
        self.assertEquals(3, len(matriz.matriz[1]))
        self.assertEquals(3, len(matriz.matriz[2]))
        self.assertEquals(3, len(matriz.matriz[3]))
        
    def test_cria_matriz_2x2(self):
        matriz = matriz_espiral(2,2)
        self.assertEquals(2, len(matriz.matriz))

    def test_primeiro_elemento(self):
        matriz = matriz_espiral(1,1)
        self.assertEquals(1,matriz.matriz[0][0])

    def test_segundo_elemento(self):
        matriz = matriz_espiral(2,2)
        self.assertEquals(2,matriz.matriz[0][1])

    def test_segundo_elemento_segunda_linha(self):
        matriz = matriz_espiral(2,2)
        self.assertEquals(3,matriz.matriz[1][1])
    
    def test_ultimo_elemento_4x3(self):
        matriz = matriz_espiral(4,3)
        self.assertEquals(6,matriz.matriz[2][3])
        
if __name__ == '__main__':
    unittest.main()
