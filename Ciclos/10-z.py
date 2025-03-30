x = 10
algoritmo = ""
for i in range(x):
    algoritmo = algoritmo + "*"
print(algoritmo)


for i in range(x):
    algoritmo = ""
    for j in range(x-i):
        algoritmo = algoritmo + " "
    algoritmo = algoritmo + "*"
    print(algoritmo)


algoritmo = ""
for i in range(x):
    algoritmo = algoritmo + "*"
print(algoritmo)