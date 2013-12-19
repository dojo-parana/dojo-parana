#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest
import torre
from torre import Pino, Disco


class pinoTeste(unittest.TestCase):
    def test_pino_existe(self):
        pino = Pino()
        self.assertTrue(pino)

    def test_disco_existe(self):
        disco = Disco()
        self.assertTrue(disco)



if __name__ == '__main__':
    unittest.main()	
