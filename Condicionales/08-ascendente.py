def numeros():
    
    num1 = int(input("Digite el primer numero: "))
    num2 = int(input("Digite el segundo numero: "))
    num3 = int(input("Digite el tercer numero: "))
    

    max_num = max(num1, num2, num3)
    min_num = min(num1, num2, num3)
    
 
    print("Números en forma ascendente:")
    print(min_num)
    print(num1 + num2 + num3 - min_num - max_num)
    print(max_num)
    
    
    print("Números en forma descendente:")
    print(max_num)
    print(num1 + num2 + num3 - min_num - max_num)
    print(min_num)
    

if __name__ == "__main__":
    numeros()
