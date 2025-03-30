temperatura = float(input("ingrese una temperatura, despues una escala:"))
escala = input("¿Es fahrenheit(F), Celsius (C), Kelvin(K), Rankine(R) o Réaumur(M) ? :").lower()


if escala == "f":
    celsius = (temperatura -32) * 5/9
    kelvin = (temperatura + 459.67) * 5/9
    rankine = (temperatura + 459.67)
    réaumur = (temperatura -32) *4/9
    
    print("De farenhait a celsius son: ", celsius)
    print("De farenhait a kelvin son: ", kelvin)
    print("De farenhait a rankine son: ", rankine)
    print("De farenhait a réaumur son: ", réaumur)
    
    
    
elif escala == "c":
    fahrenheit = (temperatura * 9/5) + 32
    kelvin = (temperatura + 273.15)
    rankine = (temperatura + 273.15) * 9/5
    réaumur = (temperatura * 4/5)
    
    
    print("De Celsius a fahrenheit son: ", fahrenheit)
    print("De Celsius a kelvin son: ", kelvin)
    print("De Celsius a rankine son: ", rankine)
    print("De Celsius a réaumur son: ", réaumur)
    
    
       
elif escala == "k":
    fahrenheit = (temperatura * 9/5) - 459.67
    celsius = (temperatura - 273.15)
    rankine = (temperatura * 9/5)
    réaumur = (temperatura - 273.15) * 4/5
    
    
    print("De Kelvin a Farenheit son: ", fahrenheit)
    print("De Kelvin a Celsius son: ", celsius)
    print("De Kelvin a Rankine son: ", rankine)
    print("De Kelvin a Réaumur son: ", réaumur)
    
    
elif escala == "r":
    fahrenheit = (temperatura - 459.67) 
    celsius = (temperatura - 459.67) * 5/9
    kelvin = (temperatura * 5/9)
    réaumur = (temperatura - 459.67 - 32 ) * 5/9 * 4/5
    
    
    print("De Rankine a Farenheit son: ", fahrenheit)
    print("De Rankine a Celsius son: ", celsius)
    print("De Rankine a Kelvin son: ", kelvin)
    print("De Rankine a Réaumur son: ", réaumur)
    
    
elif escala == "m":
    fahrenheit = (temperatura * 9/4)+ 32
    celsius = (temperatura * 5/4)
    kelvin = (temperatura * 5/4) + 273.15
    rankine =(temperatura * 9/4)+ 491.67
    
    
    print("De Réaumur a Farenheit son: ", fahrenheit)
    print("De Réaumur a Celsius son: ", celsius)
    print("De Réaumur a kelvin son: ", kelvin)
    print("De Réaumur a Rankine son: ", rankine)
    
    
    
else: "Escala incorrecta"