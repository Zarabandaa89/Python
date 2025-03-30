class Potencia:
    def potencia(self, x, n):
        return x ** n

calculadora = Potencia()
resultado = calculadora.potencia(4, 3)

print("El resultado de 4 elevado a la 3 es:", resultado)