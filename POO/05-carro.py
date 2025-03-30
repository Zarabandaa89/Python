class Carro:
    def __init__(self, marca, modelo, color, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def acelerar(self, subir_velocidad):
        self.velocidad += subir_velocidad

    def frenar(self, bajar_velocidad):
        if self.velocidad -bajar_velocidad >= 0:
            self.velocidad -=bajar_velocidad
        else:
            print("El carro ya se encuentra detenido.")

    def velocidad2(self):
        return self.velocidad

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h"
    
mi_carro = Carro(marca="Renault", modelo="Twingo", color="Gris")
print(mi_carro)

mi_carro.acelerar(100)
print("Velocidad actual:", mi_carro.velocidad2(), "km/h")

mi_carro.frenar(10)
print("Velocidad actual:", mi_carro.velocidad2(), "km/h")