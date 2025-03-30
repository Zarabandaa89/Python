
class Ave:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def volar(self):
        return f"{self.nombre} está volando."
    
    


class paloma(Ave):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

    def sonido(self):
        return f"{self.nombre} está sonando: GRRR" 
    
    
    
    

class cuervo(Ave):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
        
        
        

    def Sonido2(self):
        return f"{self.nombre} está sonando: BRRR."
    
    
mi_paloma = paloma("Paloma", "Gris")
mi_cuervo = cuervo("Cuervo", "Negro")



print(mi_paloma.volar())
print(mi_paloma.sonido())

print(mi_cuervo.volar())
print(mi_cuervo.Sonido2())
