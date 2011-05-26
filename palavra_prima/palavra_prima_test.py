import unittest
from palavra_prima import palavra_prima

class palavra_primaTest(unittest.TestCase):
  def test_create_palavra_prima(self):
    self.assertNotEqual(palavra_prima(), None)

if __name__ == '__main__':
    unittest.main()
    