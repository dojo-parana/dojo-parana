#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from telefone import Telefone

class TestTelefone(unittest.TestCase):
    def setUp(self):
        self.telefone = Telefone()

    def tearDown(self):
        pass

    def test_classe_telefone_existe(self):
        self.assertTrue(self.telefone)

    def test_entrada_telefone(self):
        self.assertEqual(
            "ABC",
            self.telefone.ler_entrada("ABC")
        )

    def test_converte_letra_a_retorna_2(self):
        self.assertEqual(
            '2',
            self.telefone.converte_letra("A")

        )

    def test_converte_letra_d_retorna_3(self):
        self.assertEqual(
            '3',
            self.telefone.converte_letra("D")
        )




if __name__ == '__main__':
    unittest.main()