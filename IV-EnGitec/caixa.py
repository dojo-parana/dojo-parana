#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2011-03-15 20:30:39
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest


class Caixa:
    def __init__(self):
        self.notas_padrao = [10,20,50,100]

    def sacar(self,valor):
        if valor in self.notas_padrao:
			return {valor:1}
        else:
		    return False
		
 
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

if __name__ == '__main__':
    unittest.main()
