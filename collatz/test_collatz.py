#!/usr/bin/env python
# coding=utf-8

import unittest
from collatz import Collatz

class TestCollatz(unittest.TestCase):
    def test_inic_classe(self):
        self.assertTrue(Collatz())

    def test_dois_deve_retornar_dois_um(self):
        self.assertEqual(Collatz().retorna_sequencia(2), (2,1))

    def test_quatro_retorna_quatro_dois_um(self):
        self.assertEqual(Collatz().retorna_sequencia(4), (4,2,1))

    def test_oito_retorna_oito_quatro_dois_um(self):
        self.assertEqual(Collatz().retorna_sequencia(8), (8,4,2,1))

    def test_dezesseis_retorna_dezesseis_oito_quatro_dois_um(self):
        self.assertEqual(Collatz().retorna_sequencia(16), (16,8,4,2,1))

    def test_impar(self):
        self.assertEqual(Collatz().retorna_sequencia(5), (5,16,8,4,2,1))

if __name__ == '__main__':
    unittest.main()