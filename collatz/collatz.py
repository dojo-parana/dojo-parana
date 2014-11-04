#!/usr/bin/env python
# coding=utf-8

class Collatz(int):

    def __init__(self, valor):
        self = valor

    def retorna_sequencia(self):
        res=[]
        valor = self

        while valor != 1:
            res.append(valor)

            if valor % 2 == 0:
               valor = valor/2
            else:
               valor = (valor * 3) + 1
        res.append(1)
        return tuple(res)

    def maior_sequencia(self):
        maior = tuple()
        for numero in range(self):
            sequencia = Collatz(numero+1).retorna_sequencia()
            if len(sequencia) > len(maior):
                maior = sequencia

        return maior