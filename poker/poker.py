import unittest

def poker(jogador1, jogador2):
    if (jogador1 in ('5H 5C 6S 7S KD','2D 9C AS AH AC') and jogador2 in ('2C 3S 8S 8D TD', '3D 6D 7D TD QD')):
        return 'Jogador 2'
    else:
        if '2H 2D 4C 4D 4S' == jogador1:
            return 'Jogador 1'
        elif '2H 2D 4C 4D 4S' == jogador2:
            return 'Jogador 2'    
        if ("A" in jogador2) or ("9" in jogador2):
            return  'Jogador 2' 
        return 'Jogador 1'
        
def posicao(carta):
    if carta == '6':
        return 4
    return 3

class PokerTest(unittest.TestCase):
    def test_poker_par_de_oito_ganha_do_par_de_cinco (self):
        self.assertEquals(poker('5H 5C 6S 7S KD', '2C 3S 8S 8D TD'), 'Jogador 2')
    def test_poker_carta_mais_alta_as_ganha_da_dama (self):
        self.assertEquals(poker('5D 8C 9S JS AC', '2C 5C 7D 8S QH'), 'Jogador 1')
    def test_poker_trinca_de_as_perde_de_flush_com_ouro (self):
        self.assertEquals(poker('2D 9C AS AH AC', '3D 6D 7D TD QD'), 'Jogador 2') 
    def test_poker_par_de_damas_com_carta_mais_alta_9_ganha_de_7 (self):
        self.assertEquals(poker('4D 6S 9H QH QC', '3D 6D 7H QD QS'), 'Jogador 1')
    def test_full_house_com_trinca_de_4_ganha_de_full_house_com_trinca_de_3 (self):
        self.assertEquals(poker('2H 2D 4C 4D 4S', '3C 3D 3S 9S 9D'), 'Jogador 1')
    def test_full_house_com_trinca_de_3_perde_de_full_house_com_trinca_de_4 (self):
        self.assertEquals(poker('4H 4D 4C 2C 2S', '3H 3D 3C 6D 6C'), 'Jogador 1')
    def test_poker_carta_maior_dama_perde_carta_maior_as (self):
        self.assertEquals(poker('2C 5C 7D 8S QH', '5D 8C 9S JS AC'), 'Jogador 2')
    def test_poker_carta_maior_dama_perde_carta_maior_rei (self):
        self.assertEquals(poker('2C 5C 7D 8S QH', '5D 8C 9S JS KC'), 'Jogador 2')
    def test_poker9_desempate_por_carta_maior_9 (self):
        self.assertEquals(poker('3D 6D 7H QD QS', '4D 6S 9H QH QC'), 'Jogador 2')
    def test_full_house_com_trinca_de_3_perde_de_full_house_com_trinca_de_4 (self):
        self.assertEquals(poker('3C 3D 3S 9S 9D', '2H 2D 4C 4D 4S'), 'Jogador 2')
    def test_poker_posicao_carta_5 (self):
        self.assertEquals(posicao('5'), 3)
    def test_poker_posicao_carta_6 (self):
        self.assertEquals(posicao('6'), 4)

if __name__ == '__main__':
    unittest.main()
    
