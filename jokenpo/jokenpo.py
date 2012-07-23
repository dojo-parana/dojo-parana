#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2012-07-23 14:23:17
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class EJogadaInvalida(Exception):
    pass

class Papel():
    def __init__(self):
        self.nome = 'Papel'

    def __lt__(self, obj):
        if obj.nome == 'Tesoura':
            return True
        else:
            return False

    def __eq__(self, obj):
        if obj.nome == self.nome:
            return True
        else:
            return False

class Pedra():
    def __init__(self):
        self.nome = 'Pedra'

    def __lt__(self, obj):
        if obj.nome == 'Papel':
            return True
        else:
            return False

    def __eq__(self, obj):
        if obj.nome == self.nome:
            return True
        else:
            return False

class Tesoura():
    def __init__(self):
        self.nome = 'Tesoura'

    def __lt__(self, obj):
        if obj.nome == 'Pedra':
            return True
        else:
            return False

    def __eq__(self, obj):
        if obj.nome == self.nome:
            return True
        else:
            return False

class jokenpo:       
    def jogada(self, j1, j2):
        parametros = [j1, j2]
        parametros.sort()
        
        for par in parametros:
            if isinstance(par, Papel) or \
               isinstance(par, Pedra) or \
               isinstance(par, Tesoura): 
                if par.nome not in ("Tesoura", "Papel", "Pedra"):
                    raise EJogadaInvalida
            else:
                raise EJogadaInvalida


        if parametros[0] == parametros[1]:
            return 'Empate'
        elif parametros[0] < parametros[1]:
            return parametros[1].nome
        else:
            return parametros[0].nome
            

class jokenpoTest(unittest.TestCase):   
    def setUp(self):
        self.j = jokenpo()
        self.papel = Papel()
        self.pedra = Pedra()
        self.tesou = Tesoura()

    def test_empate_papel_papel(self):
        j1 = self.papel
        j2 = self.papel
        self.assertEqual(self.j.jogada(j1,j2), 'Empate')

    def test_empate_pedra_pedra(self):
        j1 = self.pedra
        j2 = self.pedra
        self.assertEqual(self.j.jogada(j1,j2), 'Empate')

    def test_empate_tesoura_tesoura(self):
        j1 = self.tesou
        j2 = self.tesou
        self.assertEqual(self.j.jogada(j1,j2), 'Empate')

    def test_tesoura_vence_papel(self):
        j1 = self.tesou
        j2 = self.papel
        self.assertEqual(self.j.jogada(j1,j2), 'Tesoura')

    def test_papel_perde_tesoura(self):
        j1 = self.papel
        j2 = self.tesou
        self.assertEqual(self.j.jogada(j1,j2), 'Tesoura')
    
    def test_pedra_vence_tesoura(self):
        j1 = self.pedra
        j2 = self.tesou
        self.assertEqual(self.j.jogada(j1,j2), 'Pedra')

    def test_tesoura_perde_pedra(self):
        j1 = self.tesou
        j2 = self.pedra
        self.assertEqual(self.j.jogada(j1,j2), 'Pedra')
    
    def test_papel_vence_pedra(self):
        j1 = self.papel
        j2 = self.pedra
        self.assertEqual(self.j.jogada(j1,j2), 'Papel')

    def test_pedra_perde_papel(self):
        j1 = self.pedra
        j2 = self.papel
        self.assertEqual(self.j.jogada(j1,j2), 'Papel')

    def test_jogada_invalida(self):
        self.assertRaises(EJogadaInvalida, self.j.jogada,'Fogo','Agua')

if __name__ == '__main__':
    unittest.main()
