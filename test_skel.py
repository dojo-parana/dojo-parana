#!/usr/bin/env python3

import unittest

def traduz(palavra):
    return '2'

class TestCelular(unittest.TestCase):
    def test_A_deve_retornar_2(self):
        esperado = '2'
        
        self.assertEqual(traduz('A'), esperado)


if __name__ == '__main__':
    unittest.main()
