#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2011-03-15 20:30:39
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class Caixa:
    def __init__(self):
        pass
    
    def sacar_notas(self, valor):
        notas = []
        
        if valor >= 100:
            for x in xrange(valor/100):
                notas.append(100)
                valor -= 100
                    
        if valor >= 50:
            for x in xrange(valor/50):
                notas.append(50)        
                valor -= 50
                
        if valor >= 20:
            for x in xrange(valor/20):
                notas.append(20)
                valor -=20    
        if valor >= 10:
            for x in xrange(valor/10):
                notas.append(10)
                valor -= 10

            
        return notas
    
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

if __name__ == '__main__':
    unittest.main()
