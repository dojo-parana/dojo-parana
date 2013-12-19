#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Pino(object):
    def __init__(self, numero):
        self.numero = numero
        self.discos = []
        self.adicionaDisco(Disco(1))
        self.adicionaDisco(Disco(2))
        self.adicionaDisco(Disco(3))

    def adicionaDisco(self, disco):
        self.discos.append(disco)

class Disco(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho

class Tabuleiro(object):
    def __init__(self):
        self.pinos = []
        self.adicionaPino(Pino(1))
        self.adicionaPino(Pino(2))
        self.adicionaPino(Pino(3))
        self.pino = Pino(1)
        self.pino.adicionaDisco(Disco(3))
        self.pino.adicionaDisco(Disco(2))
        self.pino.adicionaDisco(Disco(1))


    def adicionaPino(self, pino):
        self.pinos.append(pino)