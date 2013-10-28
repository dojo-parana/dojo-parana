#!/usr/bin/env python
# -*- coding=utf-8 -*-

equipe = {
    'Renato': { 
        'Marguerita' : 4, 
        'Quatro queijos' : 5, 
        'Escarola' : 4, 
        'Portuguesa' : 5, 
        'Frango+Catupiry' : 4, 
        'Napolitana' : 3},
    'Marcelo': { 
        'Marguerita' : 2,
        'Quatro queijos' : 2,
        'Escarola' : 1,
        'Portuguesa' : 3,
        'Frango+Catupiry' : 5,
        'Napolitana' : 2 },
    'Lenon' : {
        'Marguerita' : 4,
        'Quatro queijos' : 5,
        'Escarola' : 2,
        'Portuguesa' : 1,
        'Frango+Catupiry' : 1,
        'Napolitana' : 3 },
    'Renata' : {
        'Marguerita' : 4,
        'Quatro queijos' : 5,
        'Escarola' : 1,
        'Portuguesa' : 1,
        'Frango+Catupiry' : 3,
        'Napolitana' : 4 },
    'Washington' : {
        'Marguerita' : 1,
        'Quatro queijos' : 1,
        'Escarola' : 2,
        'Portuguesa' : 3,
        'Frango+Catupiry' : 4,
        'Napolitana' : 3 },
    'Tino' : {
        'Marguerita' : 1,
        'Quatro queijos' : 5,
        'Escarola' : 1,
        'Portuguesa' : 4,
        'Frango+Catupiry' : 3,
        'Napolitana' : 2 },
    'Luca' : {
        'Marguerita' : 5,
        'Quatro queijos' : 4,
        'Escarola' : 3,
        'Portuguesa' : 4,
        'Frango+Catupiry' : 3,
        'Napolitana' : 2 }
    }

def compatibilidade(nome):
    dists = [] 
    for nome2 in equipe.keys():
        
        if nome2 == nome:
            continue
        dists.append((nome2, distancia(equipe[nome], equipe[nome2])))
    encontrado = sorted(dists, key=lambda x: x[1])[0]
    nome = encontrado[0]
    return nome

def distancia(membro1, membro2):
    acc = 0
    for sabor in membro1.keys():
        dist = membro2[sabor] - membro1[sabor]
        acc += dist**2
    return acc


