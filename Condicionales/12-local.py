try:
    cantidad_articulos = int(input("Ingrese la cantidad de artículos que va a comprar: "))
    
    unidad = float(input("Ingrese el precio unitario del producto: "))

    if cantidad_articulos <= 0 or unidad <= 0:
        print("Ingrese valores válidos para la cantidad de artículos y el precio unitario.")
        
        
    else:
        
        if cantidad_articulos > 5 and cantidad_articulos < 10:
            precio_unitario_descuento = unidad * 0.95
            
            
        elif cantidad_articulos >= 10:
            precio_unitario_descuento = unidad * 0.92
            
            
        else:
            precio_unitario_descuento = unidad

        total_a_pagar = precio_unitario_descuento * cantidad_articulos
        print("El valor total a pagar es: $ ", total_a_pagar)

except ValueError:
    print("Ingrese valores numéricos válidos para la cantidad de artículos y el precio unitario.")
