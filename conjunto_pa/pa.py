#!/usr/bin/env python
# -*- coding=utf-8 -*-



class ConjuntoPa():
    def __init__(self, conjunto):
        self.conjunto = conjunto
        self.razoes = set()

    def razao(self,num1,num2):
        return num2-num1

    def calcula_razoes(self):
        return set([0])

