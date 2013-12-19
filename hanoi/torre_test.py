#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest
from torre import Pino
from torre import Disco
from torre import Tabuleiro


class pinoTeste(unittest.TestCase):
    def setUp(self):
        self.tabuleiro = Tabuleiro()

    def test_pino_existe(self):
        pino = Pino(1)
        self.assertEqual(1, pino.numero)

    def test_disco_existe(self):
        disco = Disco(1)
        self.assertEqual(1, disco.tamanho)

    def test_discos_no_pino(self):
        self.assertEqual(3, len(self.tabuleiro.pinos[0].discos))

    def test_tabuleiro_existe(self):
        tabuleiro = Tabuleiro()
        self.assertTrue(tabuleiro)

    def test_pinos_no_tabuleiro(self):
        tabuleiro = Tabuleiro()
        self.assertEqual(3, len(self.tabuleiro.pinos))

if __name__ == '__main__':
    unittest.main()	
