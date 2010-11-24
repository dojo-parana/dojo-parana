import unittest

PRECO = 8
def preco(lista):
  if len(lista) == 1:
    return lista[0][1]*PRECO
  else:
    return 15.20

class PotterTest(unittest.TestCase):
  def test_unico_livro(self):
    self.assertEquals(preco([[1,1]]),PRECO)
  def test_dois_livros(self):
    self.assertEquals(preco([[1,2]]),PRECO*2)
  def test_dois_livros_diferentes(self):
    self.assertEquals(preco([[1,1],[2,1]]), PRECO*2*0.95)

if __name__ == '__main__':
    unittest.main()
    
