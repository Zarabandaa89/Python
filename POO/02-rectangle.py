class Rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura
    
    def calcular_area(self):
        return self.longitud * self.anchura
  
rectangulo = Rectangle(7, 4)


area = rectangulo.calcular_area()


print("El área del rectángulo es:", area)