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
        self._total = self.quantidade * self.preco

        if self.quantidade == 2:
            self._total *= 0.95
        else:
            self._total *= 0.9
        return self._total