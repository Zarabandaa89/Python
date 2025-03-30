def pago ():
    valorCuenta = float(input("Digite el valor de la cuenta:"))
    return valorCuenta
 
if __name__ == "__main__":
    metodoPago = pago()
    
if metodoPago < 150000:
    print("Debe pagar en efectivo")
elif 150000 < metodoPago <= 300000:
    print("Debe pagar con celular (Dinero electronico):")
elif 300000 < metodoPago <= 600000:
    print("Debe pagar con tarjeta debito")
else:
    print("Paga con tarjtea de credito")