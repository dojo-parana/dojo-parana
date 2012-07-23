#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# automatically created by Dojo Polyglot Environ on 2012-07-23 14:23:17
# https://github.com/afurlan/dojo-polyglot-environ

import unittest2 as unittest

class jokenpo:
    def __init__(self):
        pass

    def jogada(self, j1, j2):
        if j1 == j2:
            return 'Empate'
        else:
            if (((j1 == 'Tesoura' ) and (j2 == 'Papel' )) or 
               ((j1 == 'Papel' ) and (j2 == 'Tesoura' ))):
                return 'Tesoura'
            else:
                if (((j1 == 'Pedra' ) and (j2 == 'Tesoura' )) or 
                   ((j1 == 'Tesoura' ) and (j2 == 'Pedra' ))):
                    return 'Pedra'
            

class jokenpoTest(unittest.TestCase):
    def test_init(self):
        self.assertNotEqual(jokenpo(), None)

    def test_empate_papel_papel(self):
        self.assertEqual(jokenpo().jogada('Papel','Papel'), 'Empate')

    def test_empate_pedra_pedra(self):
        self.assertEqual(jokenpo().jogada('Pedra','Pedra'), 'Empate')

    def test_empate_tesoura_tesoura(self):
        self.assertEqual(jokenpo().jogada('Tesoura','Tesoura'), 'Empate')

    def test_tesoura_vence_papel(self):
        self.assertEqual(jokenpo().jogada('Tesoura','Papel'), 'Tesoura')

    def test_papel_perde_tesoura(self):
        self.assertEqual(jokenpo().jogada('Papel','Tesoura'), 'Tesoura')
    
    def test_pedra_vence_tesoura(self):
        self.assertEqual(jokenpo().jogada('Pedra','Tesoura'), 'Pedra')
    def test_tesoura_perde_pedra(self):
        self.assertEqual(jokenpo().jogada('Tesoura','Pedra'), 'Pedra')
    


if __name__ == '__main__':
    unittest.main()
