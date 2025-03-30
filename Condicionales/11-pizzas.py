try:
    
    print("Tamaños de pizza:")
    print("1 - Pequeña ($15.000)")
    print("2 - Mediana ($24.000)")
    print("3 - Grande ($36.000)")

    tamaño_pizza = int(input("Ingrese el número correspondiente al tamaño de la pizza que desea comprar: "))


    if tamaño_pizza < 1 or tamaño_pizza > 3:
        print("Ingrese un número válido de tamaño de pizza.")
        
    else:
        
        ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales que desea agregar: "))

       
        if ingredientes_adicionales < 0:
            print("Ingrese un número válido de ingredientes adicionales.")
        
        else:
            
            
            if tamaño_pizza == 1:
                precio = 15000
                
                
            elif tamaño_pizza == 2:
                precio = 24000
                
                
            else:
                precio= 36000

           
            precio_total = precio + (ingredientes_adicionales * 4000)

        
            print("El precio total a pagar es: $",precio_total)

except ValueError:
    print("Ingrese un número válido.")

    