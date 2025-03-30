try:
    peso_kg = float(input("Ingrese su peso en kg: "))
    estatura_metros = float(input("Ingrese su estatura en metros: "))

    if peso_kg <= 0 or estatura_metros <= 0:
        print("Ingrese valores válidos para el peso y la estatura.")
    else:

        imc = peso_kg / (estatura_metros ** 2)

       
        print("Su IMC (indice de masa corporal) es:", imc)

       
        if imc < 18.5:
            print("Estado: Bajo peso")
            
            
        elif 18.5 <= imc < 24.9:
            print("Estado: Peso normal")
            
            
        elif 25 <= imc < 29.9:
            print("Estado: Sobrepeso")
            
            
        else:
            print("Estado: Obesidad")

except ValueError:
    print("Ingrese valores numéricos válidos para el peso y la estatura.")
