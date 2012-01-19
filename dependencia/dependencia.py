#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2012-01-19 20:34:12
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class Dependencia:
    def __init__(self):
        pass
    
    def resolve(self, lista):
        return ["B","C"]

class DependenciaTest(unittest.TestCase):
    
    def test_init(self):
        self.assertNotEqual(Dependencia(), None)
    
    def test_expressao(self):
                 
        lista = ["A", ["B", "C"]]
        depend = Dependencia()
        self.assertEqual(depend.resolve(lista), ["B","C"])
        

if __name__ == '__main__':
    unittest.main()
