#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Telefone:
    def __init__(self):
        self.dicionario = {"A":'2', "B":'2', "C":'2',
                           "D":'3', "E":'3', "F":'3',
                           "G":'4', "H":'4', "I":'4',
                           "J":'5', "K":'5', "L":'5',
                           "M":'6', "N":'6', "O":'6',
                           "P":'7', "Q":'7', "R":'7', "S":'7',
                           "T":'8', "U":'8', "V":'8',
                           "W":'9', "X":'9', "Y":'9', "Z":'9'}

    def ler_entrada(self, entrada):
        return entrada

    def converte_letra(self, letra):
        return self.dicionario[letra]