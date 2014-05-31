#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from telefone import Telefone

class TestTelefone(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_classe_telefone_existe(self):
        telefone = Telefone()
        self.assertTrue(telefone)


if __name__ == '__main__':
    unittest.main()