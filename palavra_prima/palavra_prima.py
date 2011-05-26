class palavra_prima(str):
	
    def codigo(self):
        if self.isupper():
            return ord(self)-38
        else:
            return ord(self)-96    
    
  
