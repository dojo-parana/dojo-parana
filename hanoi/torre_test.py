#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest
import torre
from torre import Pino


class pinoTeste(unittest.TestCase):
    def test_exemplo(self):
        pino = Pino()
        self.assertTrue(pino)


if __name__ == '__main__':
    unittest.main()	
