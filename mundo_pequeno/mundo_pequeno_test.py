import unittest
from mundo_pequeno import mundo_pequeno

class mundo_pequenoTest(unittest.TestCase):

  def test_distancia(self):
    self.m = mundo_pequeno()
    self.assertEqual(self.m.calcula_distancia((0,0),(3,4)), 5)

if __name__ == '__main__':
    unittest.main()
    
