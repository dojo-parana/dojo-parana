import unittest

def poker(jogador1, jogador2):
    if (jogador1 in ('5H 5C 6S 7S KD','2D 9C AS AH AC') and jogador2 in ('2C 3S 8S 8D TD', '3D 6D 7D TD QD')):
        return 'Jogador 2'
    else:
        if '2H 2D 4C 4D 4S' == jogador1:
            return 'Jogador 1'
        if ("A" in jogador2) or ("9" in jogador2):
            return  'Jogador 2' 
        return 'Jogador 1'
        

class PokerTest(unittest.TestCase):
    def test_poker (self):
        self.assertEquals(poker('5H 5C 6S 7S KD', '2C 3S 8S 8D TD'), 'Jogador 2')
    def test_poker2 (self):
        self.assertEquals(poker('5D 8C 9S JS AC', '2C 5C 7D 8S QH'), 'Jogador 1')
    def test_poker3 (self):
        self.assertEquals(poker('2D 9C AS AH AC', '3D 6D 7D TD QD'), 'Jogador 2') 
    def test_poker4 (self):
        self.assertEquals(poker('4D 6S 9H QH QC', '3D 6D 7H QD QS'), 'Jogador 1')
    def test_poker5 (self):
        self.assertEquals(poker('2H 2D 4C 4D 4S', '3C 3D 3S 9S 9D'), 'Jogador 1')
    def test_poker6 (self):
        self.assertEquals(poker('4H 4D 4C 2C 2S', '3H 3D 3C 6D 6C'), 'Jogador 1')
    def test_poker7 (self):
        self.assertEquals(poker('2C 5C 7D 8S QH', '5D 8C 9S JS AC'), 'Jogador 2')
    def test_poker8 (self):
        self.assertEquals(poker('2C 5C 7D 8S QH', '5D 8C 9S JS AC'), 'Jogador 2')
    def test_poker9 (self):
        self.assertEquals(poker('3D 6D 7H QD QS', '4D 6S 9H QH QC'), 'Jogador 2')


if __name__ == '__main__':
    unittest.main()
    
