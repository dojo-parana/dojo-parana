#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest

import pizza

class PizzaTest(unittest.TestCase):
    def test_luca_deve_ser_renato(self):
        self.assertEqual(pizza.compatibilidade('Luca'), 'Renato')

if __name__ == '__main__':
    unittest.main()
