try:
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su género (f) para femenino, (m) para masculino: ")

    if genero == "f":
        pulsaciones = (220 - edad) / 10
        print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es:", pulsaciones)
        
    elif genero == "m":
        pulsaciones = (210 - edad) / 10
        print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es:", pulsaciones)
    
    else:
        print("Ingrese un valor válido para el género ((f) para femenino, (m) para masculino).")

except ValueError:
    print("Ingrese un valor numérico válido para la edad.")
