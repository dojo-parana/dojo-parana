#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2012-07-23 14:23:17
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class jokenpo:
    def __init__(self):
        pass

    def jogada(self, j1, j2):
        return 'Empate'

class jokenpoTest(unittest.TestCase):
    def test_init(self):
        self.assertNotEqual(jokenpo(), None)

    def test_empate_papel_papel(self):
        self.assertEqual(jokenpo().jogada('Papel','Papel'), 'Empate')

    def test_empate_pedra_pedra(self):
        self.assertEqual(jokenpo().jogada('Pedra','Pedra'), 'Empate')



if __name__ == '__main__':
    unittest.main()
