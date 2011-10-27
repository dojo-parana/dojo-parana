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
        if valor == 2:
            return False

class CaixaTest(unittest.TestCase):
    
    def setUp(self):
        self.caixa = Caixa()

    def test_saque_nota2(self):
        self.assertFalse(self.caixa.sacar(2))


if __name__ == '__main__':
    unittest.main()
