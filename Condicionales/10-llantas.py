try:
    cantidad_llantas = int(input("Ingrese la cantidad de llantas que desea comprar: "))
    
    if cantidad_llantas < 0:
        print("Ingrese un número válido de llantas.")
        
    else:
        
        if cantidad_llantas < 6:
            precio_unidad = 240000
            
            
        elif cantidad_llantas <= 7:
            precio_unidad = 221000
            
            
        else:
            precio_unidad = 180000
            

        total_a_pagar = precio_unidad * cantidad_llantas
        print("El valor total a pagar es: $ ",total_a_pagar)
        
        
except ValueError:
    print("Ingrese un número válido de llantas.")
