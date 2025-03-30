x = int(input("ingrese el limite del patron: "))
patron = ""
for i in range(x+2):
    patron = ""
    for j in range(1, i):
        patron = patron + (f"{j}")
    print(patron)
