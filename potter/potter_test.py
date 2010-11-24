import unittest

PRECO = 8
descontos = {2:0.95,3:0.90}
def preco(lista):

  if not lista:
    return 0
  elif len(lista) == 1:
    return lista[0][1]*PRECO
  elif len(lista) == 2:
    res = 0

    min_qtd = min(qtd for livro, qtd in lista)
    res += len(lista) * min_qtd * PRECO * 0.95
    for i in xrange(len(lista)):
      lista[i][1] -= min_qtd
    res += sum(qtd for l,qtd in lista) * PRECO

    return res
  
  else:
    res = 0

    min_qtd = min(qtd for livro, qtd in lista)
    res += len(lista) * min_qtd * PRECO * 0.90
    for i in xrange(len(lista)):
      lista[i][1] -= min_qtd
    res += sum(qtd for l,qtd in lista) * PRECO

    return res
  
#  elif len(lista) == 2:
#    return PRECO*0.95*2 + (lista[0][1] - 1) * PRECO 

class PotterTest(unittest.TestCase):

  def test_0_vol(self):
    self.assertEquals(preco([]),PRECO*0)

  def test_vol1x1(self):
    self.assertEquals(preco([[1,1]]),PRECO)

  def test_vol1x2(self):
    self.assertEquals(preco([[1,2]]),PRECO*2)

  def test_vol1x1_vol2x1(self):
    self.assertEquals(preco([[1,1],[2,1]]), PRECO*2*0.95)

  def test_vol1x2_vol2x1(self):
    self.assertEquals(preco([[1,2],[2,1]]), PRECO*2*0.95+PRECO)

  def test_vol1x3(self):
    self.assertEquals(preco([[1,3]]), PRECO*3)

  def test_vol1x3_vol2x2(self):
    self.assertEquals(preco([[1,3], [2,2]]), (PRECO*4*0.95)+PRECO)

  def test_vol1x3_vol2x1(self):
    self.assertEquals(preco([[1,3], [2,1]]), (PRECO*2*0.95)+PRECO*2)

  def test_vol1x1_vol2x1_vol3x1(self):
    self.assertEquals(preco([[1,1], [2,1], [3,1]]), (PRECO*3*0.90))

  def test_vol1x2_vol2x1_vol3x1(self):
    self.assertEquals(preco([[1,2], [2,1], [3,1]]),(PRECO*3*0.90) + PRECO)

  def test_vol1x4_vol2x1_vol3x1(self):
    self.assertEquals(preco([[1,4], [2,1], [3,1]]),(PRECO*3*0.90) + PRECO*3)
if __name__ == '__main__':
    unittest.main()
    
