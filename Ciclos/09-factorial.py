x = int(input("ingrese el numero a calcular el factorial: "))
factorial = 1
for i in range(1, x+1):
    factorial = factorial * i
print(f"el factorial del numero es: {factorial}")