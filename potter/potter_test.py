import unittest

class Potter:
  def __init__(self):
    pass
  def preco(self,lista):
    return 8

class PotterTest(unittest.TestCase):
  def test_create_potter(self):
    self.assertNotEqual(Potter(), None)
  def test_unico_livro(self):
    self.assertEquals(Potter().preco([1]),8)

if __name__ == '__main__':
    unittest.main()
    
