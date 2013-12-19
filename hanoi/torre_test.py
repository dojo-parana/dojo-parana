#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest
from torre import Pino
from torre import Disco
from torre import Tabuleiro


class pinoTeste(unittest.TestCase):
    def test_pino_existe(self):
        pino = Pino(1)
        self.assertEqual(1, pino.id)
        self.assertTrue(pino)

    def test_disco_existe(self):
        disco = Disco()
        self.assertTrue(disco)

    def test_tabuleiro_existe(self):
        tabuleiro = Tabuleiro()
        self.assertTrue(tabuleiro)
if __name__ == '__main__':
    unittest.main()	
