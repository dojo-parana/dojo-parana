#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2011-03-15 20:30:39
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest


class Caixa:
    def __init__(self):
        self.notas_padrao = [100,50,20,10]

    def sacar(self,valor):
        dic = {}
        aux = valor
        for nota in self.notas_padrao:
            cont = aux // nota 
            if cont:
                dic[nota] = cont
            aux = aux % nota
        if aux:
		    return False
        return dic
        
		
 
class CaixaTest(unittest.TestCase):
    
    def setUp(self):
        self.caixa = Caixa()

    def test_saque_nota2(self):
        self.assertFalse(self.caixa.sacar(2))

    def test_saque_nota10(self):
        self.assertEqual(self.caixa.sacar(10),{10:1})

    def test_saque_nota20(self):
        self.assertEqual(self.caixa.sacar(20),{20:1})

    def test_saque_nota50(self):
        self.assertEqual(self.caixa.sacar(50),{50:1})

    def test_saque_nota100(self):
        self.assertEqual(self.caixa.sacar(100),{100:1})

    def test_saque_valor30(self):
        self.assertEqual(self.caixa.sacar(30),{20:1,10:1})

    def test_saque_valor80(self):
        self.assertEqual(self.caixa.sacar(80),{50:1,20:1,10:1})

    def test_saque_valor55(self):
        self.assertFalse(self.caixa.sacar(55))

    def test_saque_valor680(self):
        self.assertEqual(self.caixa.sacar(680),{100:6,50:1,20:1,10:1})

    def test_saque_valor682(self):
        self.assertFalse(self.caixa.sacar(682))

if __name__ == '__main__':
    unittest.main()
