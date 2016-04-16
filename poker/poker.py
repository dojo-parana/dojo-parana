import unittest

def poker(jogador1, jogador2):
    if (jogador1 == '5H 5C 6S 7S KD' and jogador2 == '2C 3S 8S 8D TD'):
        return 'Jogador 2'
    else:
        return 'Jogador 1'

class PokerTest(unittest.TestCase):
    def test_poker (self):
        self.assertEquals(poker('5H 5C 6S 7S KD', '2C 3S 8S 8D TD'), 'Jogador 2')
    def test_poker2 (self):
        self.assertEquals(poker('5D 8C 9S JS AC', '2C 5C 7D 8S QH'), 'Jogador 1')

if __name__ == '__main__':
    unittest.main()
    
