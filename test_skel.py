#!/usr/bin/env python3

import unittest

def traduz(palavra):
    dicionario_saida = {
        'A':'2','B':'22','C':'222',
        'D':'3','E':'33','F':'333',
        'G':'4','H':'44','I':'444',
        'J':'5','K':'55','L':'555',
        'M':'6','N':'66','O':'666',
        'P':'7','Q':'77','R':'777', 'S': '7777',
        'T':'8','U':'88','V':'888',
        'W':'9','X':'99','Y':'999', 'Z': '9999',
        ' ':'0'
} 

    for n in palavra:       
        return dicionario_saida[n]

class TestCelular(unittest.TestCase):
    def test_A_deve_retornar_2(self):
        esperado = '2'
        self.assertEqual(traduz('A'), esperado)
    
    def test_B_deve_retornar_22(self):
        esperado = '22'
        self.assertEqual(traduz('B'), esperado)
    
    def test_C_deve_retornar_222(self):
        esperado = '222'
        self.assertEqual(traduz('C'), esperado)
       
    def test_D_deve_retornar_3(self):
        esperado = '3'
        self.assertEqual(traduz('D'), esperado)
       
    def test_E_deve_retornar_33(self):
        esperado = '33'
        self.assertEqual(traduz('E'), esperado)

    def test_F_deve_retornar_333(self):
        esperado = '333'
        self.assertEqual(traduz('F'), esperado)

        
    def test_G_deve_retornar_4(self):
        esperado = '4'
        self.assertEqual(traduz('G'), esperado)

    def test_H_deve_retornar_44(self):
        esperado = '44'
        self.assertEqual(traduz('H'), esperado)
    

    def test_J_deve_retornar_5(self):
        esperado = '5'
        self.assertEqual(traduz('J'), esperado)

    def test_K_deve_retornar_55(self):
        esperado = '55'
        self.assertEqual(traduz('K'), esperado)

    def test_L_deve_retornar_555(self):
        esperado = '555'
        self.assertEqual(traduz('L'), esperado)

    def test_M_deve_retornar_6(self):
        esperado = '6'
        self.assertEqual(traduz('M'), esperado)
    
    def test_N_deve_retornar_66(self):
        esperado = '66'
        self.assertEqual(traduz('N'), esperado)

    def test_O_deve_retornar_666(self):
        esperado = '666'
        self.assertEqual(traduz('O'), esperado)
    
    def test_P_deve_retornar_7(self):
        esperado = '7'
        self.assertEqual(traduz('P'), esperado)

    def test_Q_deve_retornar_77(self):
        esperado = '77'
        self.assertEqual(traduz('Q'), esperado)

    def test_R_deve_retornar_777(self):
        esperado = '777'
        self.assertEqual(traduz('R'), esperado)

    def test_S_deve_retornar_7777(self):
        esperado = '7777'
        self.assertEqual(traduz('S'), esperado)

    def test_T_deve_retornar_8(self):
        esperado = '8'
        self.assertEqual(traduz('T'), esperado)

    def test_U_deve_retornar_88(self):
        esperado = '88'
        self.assertEqual(traduz('U'), esperado)

    def test_V_deve_retornar_88(self):
        esperado = '888'
        self.assertEqual(traduz('V'), esperado)

    def test_W_deve_retornar_9(self):
        esperado = '9'
        self.assertEqual(traduz('W'), esperado)

    def test_X_deve_retornar_99(self):
        esperado = '99'
        self.assertEqual(traduz('X'), esperado)

    def test_Y_deve_retornar_999(self):
        esperado = '999'
        self.assertEqual(traduz('Y'), esperado)

    def test_Z_deve_retornar_9999(self):
        esperado = '9999'
        self.assertEqual(traduz('Z'), esperado)

    def test_espaco_deve_retornar_0(self):
        esperado = '0'
        self.assertEqual(traduz(' '), esperado)


if __name__ == '__main__':
    unittest.main()
