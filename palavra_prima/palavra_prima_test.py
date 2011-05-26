import unittest
from palavra_prima import palavra_prima

class palavra_primaTest(unittest.TestCase):
    def test_codigo_simples(self):
        self.assertEqual(palavra_prima("a").codigo(), 1)

    def test_codigo_maiusculo(self):
        self.assertEqual(palavra_prima("A").codigo(), 27)
	
    def test_codigo_duasletras(self):
        self.assertEqual(palavra_prima("bb").codigo(), 4)
	

if __name__ == '__main__':
    unittest.main()
    
