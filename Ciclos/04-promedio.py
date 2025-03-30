def promedio_notas():
    suma_notas = 0
    
    for distancia in range(10):
        nota = float(input(f"Digite la nota {distancia + 1}: "))
        suma_notas += nota
    print("La suma de las 10 notas es: ",suma_notas)
        
    
    promedio = suma_notas / 10
    print("Su promedio es de:",promedio)

if __name__ == "__main__":
    promedio_notas()