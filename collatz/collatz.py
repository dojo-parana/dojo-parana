#!/usr/bin/env python
# coding=utf-8

class Collatz():
   def retorna_sequencia(self, valor):
       res=[]
       while valor != 1:
           res.append(valor)

           if valor % 2 == 0:
              valor = valor/2
           else:
              valor = (valor * 3) + 1
       res.append(1)
       return tuple(res)