#!/usr/bin/env python
# -*- coding=utf-8 -*-


class PaError(Exception):
    pass


class ConjuntoPa():
    def __init__(self, conjunto):
        self.conjunto = conjunto

    def razao(self):
        if len(self.conjunto) == 1:
            raise PaError()
        if self.conjunto == (1,1):
            return 0
        return 1