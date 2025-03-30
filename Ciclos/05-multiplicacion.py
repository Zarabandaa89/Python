def tablas(numero):
    print(f"Tabla de multiplicar del {numero}:")
    
    
    for multiplicacion in range(1, 11):
        resultado = numero * multiplicacion
        print(f"{numero} x {multiplicacion} = {resultado}")

numero_ingresado = int(input("Ingrese un numero para imprimir su respectiva tabla: "))
tablas(numero_ingresado)