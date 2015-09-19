#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest

from livraria import Compras


class TestCompras(unittest.TestCase):
    def test_criacao_da_classe(self):
        compras = Compras(1)
        self.assertFalse(compras is None)
        self.assertEqual(compras.quantidade, 1)
        self.assertEqual(compras.preco, 42)

    def test_valor_da_compra_1_livro(self):
        compras = Compras(1)
        self.assertEqual(compras.total, 42)

    def test_valor_da_compra_2_livros(self):
        compras = Compras(2)
        self.assertEqual(compras.total, ((compras.quantidade * compras.preco)*0.95))

    def test_valor_da_compra_3_livros(self):
        compras = Compras(3)
        self.assertEqual(compras.total, ((compras.quantidade * compras.preco)*0.90))

    def test_valor_da_compra_4_livros(self):
        compras = Compras(4)
        self.assertEqual(compras.total, ((compras.quantidade * compras.preco)*0.85))



if __name__ == '__main__':
    unittest.main()	
