# a2 = b2 + c2

from math import sqrt

class mundo_pequeno:
  def __init__(self):
    pass

  def calcula_distancia(self, ponto1, ponto2):
    b = ponto2[0] - ponto1[0]
    c = ponto2[1] - ponto1[1]
    resultado = sqrt(b**2+c**2)	
    return resultado
