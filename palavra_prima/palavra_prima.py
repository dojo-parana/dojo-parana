import math

class palavra_prima(str):
    def codigo(self):
        soma = 0
        for caract in self:
            if caract.isupper():
                soma += ord(caract)-38           
            else:
                soma += ord(caract)-96
        return soma  

    def isprima(self):
        codigo = self.codigo()
        for i in range(2,math.sqrt(codigo)+1):
            if (codigo % i)==0:
                return False   
        return codigo != 1
     
  
