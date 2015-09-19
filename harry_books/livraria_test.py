#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest

from livraria import Compras


class TestCompras(unittest.TestCase):
    def test_modelo(self):
        compras = Compras()
        self.assertFalse(compras is None)

if __name__ == '__main__':
    unittest.main()	
