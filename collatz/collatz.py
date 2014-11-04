#!/usr/bin/env python
# coding=utf-8

class Collatz():
   def retorna_sequencia(self, valor):
       res=[]
       while valor != 1:
           res.append(valor)
           valor = valor/2
       res.append(1)
       return tuple(res)