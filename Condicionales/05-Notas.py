def Notas():
    Notas_1 = float(input("Ingrese la nota 1: "))
    Notas_2 = float(input("Ingrese la nota 2: "))
    Notas_3 = float(input("Ingrese la nota 3: "))
    Promedio_notas = (Notas_1 + Notas_2+ Notas_3) / 3
    print ("El promedio de las notas es:", Promedio_notas)
    
    if 3.0 <= Promedio_notas <= 5.0:
        print("Aprobo")
    elif Promedio_notas <= 2.9:
            print("Usted no aprobo")
    else:
        print("ERROR: el promedio debe ser menor a o igual a 5.0: ")
if __name__ == "__main__":
    Notas()