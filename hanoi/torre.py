#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Pino(object):
    def __init__(self, numero):
        self.numero = numero
        self.discos = []

    def adicionaDisco(self, disco):
        self.discos.append(disco)

class Disco(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho

class Tabuleiro(object):
    def __init__(self):
        self.pinos = []

    def adicionaPino(self, pino):
        self.pinos.append(pino)