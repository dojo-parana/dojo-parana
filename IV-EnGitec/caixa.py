#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2011-03-15 20:30:39
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest


class Caixa:
    def __init__(self):
        pass

    def sacar(self,valor):
        if valor % 10 != 0:
            return False
        if valor == 10:
            return {10:1} 
       

class CaixaTest(unittest.TestCase):
    
    def setUp(self):
        self.caixa = Caixa()

    def test_saque_nota2(self):
        self.assertFalse(self.caixa.sacar(2))

    def test_saque_nota10(self):
        self.assertEqual(self.caixa.sacar(10),{10:1})

    


if __name__ == '__main__':
    unittest.main()