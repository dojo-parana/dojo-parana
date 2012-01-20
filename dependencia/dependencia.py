#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2012-01-19 20:34:12
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class Dependencia:
        
    def resolve(self, lista):
        dependencias = {}

        for elemento in lista:
            dependencias[elemento[0]] = set(elemento[1])
                
        for chave, valor in dependencias.items():
            for subchave in valor:
                subvalor = dependencias.get(subchave)
                if subvalor:
                    dependencias[chave] = dependencias[chave].union(subvalor)
                
        return dependencias

class DependenciaTest(unittest.TestCase):
    
    def test_init(self):
        self.assertNotEqual(Dependencia(), None)
    
    def test_ABC(self):
        entrada = [["A", ["B", "C"]]]
        retorno = {"A": set(["B","C"])}
        depend = Dependencia()
        self.assertEqual(depend.resolve(entrada), retorno)

    def test_BCE(self):
        entrada = [["B", ["C", "E"]]]
        retorno = {"B": set(["C","E"])}
        depend = Dependencia()
        self.assertEqual(depend.resolve(entrada), retorno)

    def test_ABCBCE(self):
        entrada = [["A", ["B", "C"]],["B", ["C", "E"]]]
        retorno = {"A": set(["B","C","E"]), "B": set(["C","E"])}
        depend = Dependencia()
        self.assertEqual(depend.resolve(entrada), retorno)

    
        

if __name__ == '__main__':
    unittest.main()
