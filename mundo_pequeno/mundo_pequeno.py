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

  def inicializa(self, entrada):
    lista = entrada.splitlines()
    lista = [x.split() for x in lista]
    self.amigos = {}
    for x in lista:
        self.amigos[int(x[0])] = (int(x[1]),int(x[2]))
    
  def processa(self):
    resultado = []
    for chave, valor in self.amigos.iteritems():
        resultado.append((self.calcula_distancia((0,0),valor),chave))
    resultado.sort()      
    self.distancias = resultado
