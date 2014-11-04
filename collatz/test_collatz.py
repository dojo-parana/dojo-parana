#!/usr/bin/env python
# coding=utf-8

import unittest
from collatz import Collatz

class TestCollatz(unittest.TestCase):
    def test_inic_classe(self):
        self.assertTrue(Collatz())

    def test_dois_deve_retornar_dois_um(self):
        self.assertEqual(Collatz().get_sequence(2), (2,1))

if __name__ == '__main__':
    unittest.main()