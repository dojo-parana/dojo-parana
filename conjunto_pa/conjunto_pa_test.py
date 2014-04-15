#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from pa import ConjuntoPa


class TestConjuntoPa(unittest.TestCase):
    def setUp(self):
        self.pa = ConjuntoPa((1,1,))

    def test_conjunto_pa_deve_existir(self):
        self.assertTrue(self.pa.conjunto)

    def test_conjunto_pa_razao_1_1_deve_ser_0(self):
        self.assertEqual(self.pa.razao(),0)

if __name__ == '__main__':
    unittest.main()