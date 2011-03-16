#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2011-03-15 20:30:39
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest


class NotaInvalidaError(Exception):
    pass


class Caixa:
    def __init__(self):
        self.notas = [ 100, 50, 20, 10 ]
    
    def sacar_notas(self, valor):
        retorno = []
        for nota in self.notas:
            for x in xrange(valor/nota):
                retorno.append(nota)
                valor -= nota
        
        if valor != 0:
            raise NotaInvalidaError()
            
        return retorno
    
    def contar_notas(self, valor):
        return len(self.sacar_notas(valor))

class CaixaTest(unittest.TestCase):
    def test_init(self):
        self.assertNotEqual(Caixa(), None)
        
    def test_sacar_100(self):
        self.assertEqual(Caixa().sacar_notas(100), [100])
    
    def test_sacar_200(self):
        self.assertEqual(Caixa().sacar_notas(200), [100, 100])
        
    def test_sacar_300(self):
        self.assertEqual(Caixa().sacar_notas(300), [100, 100, 100])
        
    def test_sacar_50(self):
        self.assertEqual(Caixa().sacar_notas(50), [50])

    def test_sacar_20(self):
        self.assertEqual(Caixa().sacar_notas(20), [20])

    def test_sacar_40(self):
        self.assertEqual(Caixa().sacar_notas(40), [20,20])

    def test_sacar_10(self):
        self.assertEqual(Caixa().sacar_notas(10), [10])

    def test_sacar_60(self):
        self.assertEqual(Caixa().sacar_notas(60), [50, 10])
        
    def test_sacar_55(self):
        self.assertRaises(NotaInvalidaError, Caixa().sacar_notas, 55)
    
    def test_contar_notas_100(self):
        self.assertEqual(Caixa().contar_notas(100), 1)
    
    def test_contar_notas_55(self):
        self.assertRaises(NotaInvalidaError,Caixa().contar_notas, 55)
        
    def test_contar_notas_60(self):
        self.assertNotEqual(Caixa().contar_notas(60), 3)
    
    
if __name__ == '__main__':
    unittest.main()
