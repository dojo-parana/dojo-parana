#!/usr/bin/env python
# -*- coding=utf-8 -*-


class PaError(Exception):
    pass


class ConjuntoPa():
    def __init__(self, conjunto):
        self.conjunto = conjunto

    def razao(self,num1,num2):
        if len(self.conjunto) == 1:
            raise PaError()
        return num2-num1