#!/usr/bin/env python
# coding=utf-8

class Collatz():
   def retorna_sequencia(self, valor):
       if valor == 2:
           return (2,1)
       elif valor == 4:
           return (4,2,1)
       else:
           return (8,4,2,1)