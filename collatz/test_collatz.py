#!/usr/bin/env python
# coding=utf-8

import unittest

from collatz import Collatz


class TestCollatz(unittest.TestCase):
    def test_inic_classe(self):
        self.assertTrue(isinstance(Collatz(5), int))

    def test_dois_deve_retornar_dois_um(self):
        self.assertEqual(Collatz(2).retorna_sequencia(), (2,1))

    def test_quatro_retorna_quatro_dois_um(self):
        self.assertEqual(Collatz(4).retorna_sequencia(), (4,2,1))

    def test_oito_retorna_oito_quatro_dois_um(self):
        self.assertEqual(Collatz(8).retorna_sequencia(), (8,4,2,1))

    def test_dezesseis_retorna_dezesseis_oito_quatro_dois_um(self):
        self.assertEqual(Collatz(16).retorna_sequencia(), (16,8,4,2,1))

    def test_impar(self):
        self.assertEqual(Collatz(5).retorna_sequencia(), (5,16,8,4,2,1))

    def test_maior_sequencia(self):
        self.assertEqual(Collatz(5).maior_sequencia(), (3,10,5,16,8,4,2,1))




if __name__ == '__main__':
    unittest.main()