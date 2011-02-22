# -*- coding:utf-8 -*-

import unittest

class ContaLetras:
  def __init__(self):
    pass

class ContaLetrasTest(unittest.TestCase):
  def test_create_contaletras(self):
    self.assertNotEqual(ContaLetras(), None)

if __name__ == '__main__':
    unittest.main()    
