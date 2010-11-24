import unittest

def preco(lista):
  return lista[0][1]*8

class PotterTest(unittest.TestCase):
  def test_unico_livro(self):
    self.assertEquals(preco([[1,1]]),8)
  def test_dois_livros(self):
    self.assertEquals(preco([[1,2]]),16)

if __name__ == '__main__':
    unittest.main()
    
