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
        elif self.quantidade == 3:
            self._total *= 0.9
        elif self.quantidade == 4:
            self._total *= 0.85
        elif self.quantidade >= 5:
            self._total *= 0.80
        return self._total
