import math
def operacion():
    
    print("Digite el numero para calcular el area de una figura: ")
    print("1. Calcular área de cuadrado")
    print("2. Calcular área de rectángulo")
    print("3. Calcular área de triángulo")
    print("4. Calcular área de círculo")
    print("5. Calcular área de rombo")
    print("6. Calcular área de trapecio")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
            cuadrado()
    elif opcion == 2:
            rectangulo()
    elif opcion == 3:
            triangulo()
    elif opcion == 4:
            circulo()
    elif opcion == 5:
            rombo()
    elif opcion == 6:
            trapecio()
    elif opcion == 7:
            print("¡Hasta luego!")
     
     
def cuadrado():
    lado = float(input("Ingrese un lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: ", area)

def rectangulo():
    base = float(input("Ingrese un lado base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es: ", area)

def triangulo():
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: ", area)

def circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio**2
    print(f"El área del círculo es: ", area)

def rombo():
    diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
    area = (diagonal_mayor * diagonal_menor) / 2
    print(f"El área del rombo es: ",area)

def trapecio():
    base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la longitud de la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = ((base_mayor + base_menor) * altura) / 2
    print(f"El área del trapecio es: ", area)

if __name__ == "__main__":
    operacion()
