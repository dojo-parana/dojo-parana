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
        self.assertEqual(self.pa.razao(1,1,),0)

    def test_conjunto_pa_razao_1_2_deve_ser_1(self):
        self.assertEqual(self.pa.razao(1,2,),1)

    def test_conjunto_deve_ter_mais_que_um_elemento(self):
        self.pa.conjunto = (1,)
        self.assertRaises(PaError, self.pa.razao,1,5)

    def test_conjunto_pa_razao_1_3_deve_ser_2(self):
        self.assertEqual(self.pa.razao(1,3,),2)


if __name__ == '__main__':
    unittest.main()