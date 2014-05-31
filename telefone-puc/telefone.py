#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Telefone:
    def __init__(self):
        pass

    def ler_entrada(self, entrada):
        return entrada

    def converte_letra(self, letra):
        if ord(letra) >= 65 and ord(letra) < 68:
            return '2'

        if ord(letra) >= 68 and ord(letra) < 71:
            return '3'

        if ord(letra) >= 71 and ord(letra) < 74:
            return '4'

        if ord(letra) >= 74 and ord(letra) < 77:
            return '5'

        if ord(letra) >= 77 and ord(letra) < 80:
            return '6'

        if ord(letra) >= 80 and ord(letra) < 84:
            return '7'

        if ord(letra) >= 84 and ord(letra) < 87:
            return '8'