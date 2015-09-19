#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Compras(object):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.preco = 42
        self._total = 0

    @property
    def total(self):


        desconto = 1 - ((self.quantidade - 1) * 0.05)

        if desconto < 0.8:
            desconto = 0.8

        self._total = self.quantidade * self.preco * desconto
        return self._total
