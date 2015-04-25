#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest

class TestaTeclado(unittest.TestCase):
    def testa_teclas(self):
        self.assertEqual(teclas('a'), '2')


def teclas(frase):
    if frase == 'a':
        return "2"


if __name__ == '__main__':
    unittest.main()