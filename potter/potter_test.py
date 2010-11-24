import unittest

PRECO = 8
def preco(lista):

  if not lista:
    return 0
  elif len(lista) == 1:
    return lista[0][1]*PRECO

  res = 0

  min_qtd = min(qtd for livro, qtd in lista)
  res += 2 * min_qtd * PRECO * 0.95
  lista[0][1] -= min_qtd
  lista[1][1] -= min_qtd
  res += (lista[0][1] + lista[1][1]) * PRECO

  return res
  
#  elif len(lista) == 2:
#    return PRECO*0.95*2 + (lista[0][1] - 1) * PRECO 

class PotterTest(unittest.TestCase):

  def test_zero_livros(self):
    self.assertEquals(preco([]),PRECO*0)

  def test_unico_livro(self):
    self.assertEquals(preco([[1,1]]),PRECO)

  def test_dois_livros(self):
    self.assertEquals(preco([[1,2]]),PRECO*2)

  def test_dois_livros_diferentes(self):
    self.assertEquals(preco([[1,1],[2,1]]), PRECO*2*0.95)

  def test_dois_livros_diferentes_quantidades_diferentes(self):
    self.assertEquals(preco([[1,2],[2,1]]), PRECO*2*0.95+PRECO)

  def test_tres_livros_iguais(self):
    self.assertEquals(preco([[1,3]]), PRECO*3)

  def test_vol1x3_vol2x2(self):
    self.assertEquals(preco([[1,3], [2,2]]), (PRECO*4*0.95)+PRECO)

if __name__ == '__main__':
    unittest.main()
    
