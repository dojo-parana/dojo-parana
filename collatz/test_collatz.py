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

    def test_retorna_sequencia(self):
        self.assertEqual(Collatz().retorna_sequencia(8), (8,4,2,1))

if __name__ == '__main__':
    unittest.main()