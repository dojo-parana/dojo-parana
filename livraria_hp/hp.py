#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2013-02-25 19:41:35
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest


def calcula(lista):
    if lista[0][0] == 2:
        return 79.8
    return 42

class hpTest(unittest.TestCase):
    def test_uma_copia_livro_um(self):
        self.assertEqual(42, calcula([(1, 1)]))

    def test_duas_copias_livro_um(self):
        self.assertEqual((42*2)*0.95, calcula([(2,1)]))


if __name__ == '__main__':
    unittest.main()
