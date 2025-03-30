x = int(input("ingrese el limite del patron: "))
algoritmo = ""

for i in range(1, x):
    algoritmo = ""
    for j in range(i):
        algoritmo = algoritmo + "*"
    print(algoritmo)
    
    
    
for i in range(x, 0, -1):
    algoritmo = ""
    for j in range(i):
        algoritmo = algoritmo + "*"
    print(algoritmo)