import unittest
from mundo_pequeno import mundo_pequeno

class mundo_pequenoTest(unittest.TestCase):

  def test_distancia(self):
    self.m = mundo_pequeno()
    self.assertEqual(self.m.calcula_distancia((0,0),(3,4)), 5)

  def test_distancia_negativa(self):
    self.m = mundo_pequeno()
    self.assertEqual(self.m.calcula_distancia((3,4),(0,0)), 5)
  
  def test_inicializa(self):
    self.m = mundo_pequeno()
    self.m.inicializa("""1 3 4
2 -3 -4""")
    self.assertEqual(self.m.amigos, {1:(3,4),
                                     2:(-3,-4)})
  def test_processa(self):
    self.m = mundo_pequeno()
    self.m.inicializa("""1 3 4
2 -3 -4""")
    self.m.processa()
    self.assertEqual(self.m.distancias, [(5,1),(5,2)])

if __name__ == '__main__':
    unittest.main()
    
