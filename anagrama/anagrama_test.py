#!/usr/bin/env python
# -*- coding=utf-8 -*- 

import unittest

def test_anagram(palavra1, palavra2, chars):
    palavras = sorted(list(palavra1+palavra2))
    chars = sorted(list(chars))
    return palavras == chars

def read_word_list(file_name):
    fp = open(file_name)
    lines = fp.readlines()
    return [x.strip() for x in lines]

class AnagramaTest(unittest.TestCase):
    def test_anagram_test(self):
        self.assertTrue(test_anagram('a', 'b', 'ab'))
        self.assertFalse(test_anagram('a', 'x', 'ab'))
        self.assertTrue(test_anagram('ab', 'cd', 'abcd'))
        self.assertTrue(test_anagram('ac', 'bd', 'abcd'))

    def test_anagram_letras_repetidas(self):
        self.assertTrue(test_anagram('aab', 'bbc', 'aabbbc'))
        self.assertFalse(test_anagram('aab', 'bbc', 'abc'))
        self.assertFalse(test_anagram('aab', 'bcc', 'aabbbc'))

    def test_word_list(self): 
        self.assertEquals(read_word_list('wordlist.txt'), ['a', 'b'])

if __name__ == '__main__':
   unittest.main()
