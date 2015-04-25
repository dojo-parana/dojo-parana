#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest

class TestaTeclado(unittest.TestCase):
    def testa_tecla_a(self):
        self.assertEqual(teclas('a'), '2')
        self.assertEqual(teclas('A'), '2')

    def testa_tecla_b(self):
        self.assertEqual(teclas('b'), '22')
        self.assertEqual(teclas('B'), '22')


def teclas(frase):
    if frase.upper() == 'A':
        return "2"

    if frase.upper() == 'B':
        return "22"


if __name__ == '__main__':
    unittest.main()