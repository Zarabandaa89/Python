def numero():
    numero = int(input("Ingrese el primer digito: "))
    dos = int(input("ingrese el segundo digito: "))
    
    if numero > dos:
      print("El digito mayor es: ", numero)
    elif numero < dos:
        print("El digito menor es: ", numero)
    else:
        print("Los digitos son iguales: ")
if __name__ == "__main__":
    numero()