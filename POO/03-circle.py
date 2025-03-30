import math
class circle:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio**2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

circulo = circle(7)

area = circulo.area()
perimetro = circulo.perimetro()

print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)
