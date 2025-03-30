x = int(input("ingrese el numero limite del patron: "))
numero = 1
i = 0
filas = 0
while numero <= x:
    i += 1
    for j in range(i):
        numero += 1
    filas += 1
numero = 1
mostrar = ""
for j in range(1, filas + 1):
    mostrar = ""
    for w in range(filas-j):
        mostrar =mostrar + " "
    for p in range(j):
        mostrar = mostrar + (f"{numero}")
        numero += 1
        if numero > x:
            break
    print(f"{mostrar}")
