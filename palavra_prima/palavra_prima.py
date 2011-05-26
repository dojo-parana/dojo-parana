class palavra_prima(str):
	
    def codigo(self):
        soma = 0
        for caract in self:
            if self.isupper():
                soma += ord(caract)-38           
            else:
                soma += ord(caract)-96
        return soma       
  
