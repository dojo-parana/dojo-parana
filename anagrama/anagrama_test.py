#!/usr/bin/env python
# -*- coding=utf-8 -*- 

import unittest

def test_anagram(palavra1, palavra2, chars):
    for c in palavra1+palavra2:
        if not c in chars:
            return False
    return len(palavra1+palavra2) == len(chars)

class AnagramaTest(unittest.TestCase):
    def test_anagram_test(self):
        self.assertTrue(test_anagram('a', 'b', 'ab'))
        self.assertFalse(test_anagram('a', 'x', 'ab'))
        self.assertTrue(test_anagram('ab', 'cd', 'abcd'))
        self.assertTrue(test_anagram('ac', 'bd', 'abcd'))

    def test_anagram_letras_repetidas(self):
        self.assertTrue(test_anagram('aab', 'bbc', 'aabbbc'))
        self.assertFalse(test_anagram('aab', 'bbc', 'abc'))

if __name__ == '__main__':
   unittest.main()
