def positivos():
    Numero = int(input("Digite un numero (puede ser negtavio): "))
    
    if Numero > 0: 
       print("Su numero es positivo")
    elif Numero == 0:
        print("Su numero es CERO")
    elif Numero < 0:
        print("Su numero es negativo")
if __name__ == "__main__":
    positivos()