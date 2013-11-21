#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from conversor import Conversor

class TestCheque(unittest.TestCase):
    def test_um(self):
        self.assertEqual(Conversor().bla('um'), '1')
    def test_dois(self):
		self.assertEqual(Conversor().bla('dois'), '2')
    def test_tres(self):
		self.assertEqual(Conversor().bla('três'), '3')

if __name__ == '__main__':
	unittest.main()
