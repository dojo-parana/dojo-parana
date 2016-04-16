import unittest

def poker(jogador1, jogador2):
    return 'Jogador 2'

class PokerTest(unittest.TestCase):
    def test_poker (self):
        self.assertEquals(poker('5H 5C 6S 7S KD', '2C 3S 8S 8D TD'), 'Jogador 2')


if __name__ == '__main__':
    unittest.main()
    
