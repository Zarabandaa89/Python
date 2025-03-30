def Edad():
   Nombre = str(input("Digite su nombre: "))
   Edad = int(input("Digite su edad: "))
   
   print("Su Nombres es: ",Nombre)
   
   if Edad >= 18:
       print("Usted es mayor de edad")
   elif  Edad >=100: 
       print("Ingrese una edad valida") 
   else:
       print("Usted es menor de edad")
       
if __name__ == "__main__":
    Edad()