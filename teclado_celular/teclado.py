#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest

class TestaTeclado(unittest.TestCase):
    def testa_frase_a(self):
        self.assertEqual(teclas('a'), '2')
        self.assertEqual(teclas('A'), '2')

    def testa_frase_b(self):
        self.assertEqual(teclas('b'), '22')
        self.assertEqual(teclas('B'), '22')

    def testa_frase_c(self):
        self.assertEqual(teclas('c'), '222')
        self.assertEqual(teclas('C'), '222')

    def testa_frase_d(self):
        self.assertEqual(teclas('d'), '3')
        self.assertEqual(teclas('D'), '3')

def teclas(frase):
    retorno = []
    if frase.upper() == 'A':
        retorno.append("2")

    if frase.upper() == 'B':
        retorno.append("22")

    if frase.upper() == 'C':
        retorno.append("222")

    if frase.upper() == 'D':
        retorno.append("3")

    return ''.join(retorno)


if __name__ == '__main__':
    unittest.main()