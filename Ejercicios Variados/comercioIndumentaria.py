#Diseñe un programa correspondiente. En un comercio de venta de
#indumentaria, el monto final a pagar depende de la forma de pago del cliente. Si paga en efectivo se le
#descuenta un 10%. Si paga con tarjeta se le efectúa un recargo del 15%. Confeccionar un programa que
#calcule el monto total a pagar para una venta, donde se ingresa el valor del producto comprado y la
#forma de pago.

#Ingreso de datos
monto = float(input("Ingrese el precio a pagar: "))
metodo_pago = input("Ingrese la forma de pago (efectivo o targeta): ").lower()

#Verificacion de metodo de pago y calculo del monto total
if metodo_pago == "efectivo":
    monto_total = monto - (monto * 0.1)
elif metodo_pago == "targeta":
    monto_total = monto + (monto * 0.15)
else:
    raise Exception("Ingrese un metodo de pago valido") #Error generico

#Mostrar resultados
print(f"El monto total a pagar es: {monto_total}\nMetodo de pago es: {metodo_pago}")