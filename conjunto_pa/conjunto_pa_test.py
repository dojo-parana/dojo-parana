#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from pa import ConjuntoPa
from pa import PaError


class TestConjuntoPa(unittest.TestCase):
    def setUp(self):
        self.pa = ConjuntoPa((1,1,))

    def test_conjunto_pa_deve_existir(self):
        self.assertTrue(self.pa.conjunto)

    def test_conjunto_pa_razao_1_1_deve_ser_0(self):
        self.assertEqual(self.pa.razao(),0)

    def test_conjunto_pa_razao_1_2_deve_ser_1(self):
        self.pa.conjunto = (1,2,)
        self.assertEqual(self.pa.razao(),1)

    def test_conjunto_deve_ter_mais_que_um_elemento(self):
        self.pa.conjunto = (1,)
        self.assertRaises(PaError, self.pa.razao)

if __name__ == '__main__':
    unittest.main()