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
        return [100]
    
class CaixaTest(unittest.TestCase):
    def test_init(self):
        self.assertNotEqual(Caixa(), None)
        
    def test_nota100(self):
        self.assertEqual(Caixa().sacar_notas(100), [100])
            

if __name__ == '__main__':
    unittest.main()
