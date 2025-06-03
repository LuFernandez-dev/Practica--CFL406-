#Diseñe un programa, para ayudar a un cajero de
#supermercado, si el cliente tiene la tarjeta de socio en cada compra se le hace un 20% de descuento. Si
#paga con tarjeta de crédito se le aplica un recargo del 15%. Y si paga con tarjeta de débito o efectivo se
#le hace un 15% de descuento.

monto = float(input("Ingrese el total de la compra: "))

while True:
    print("1.Credito\n2.Debito\n3.Efectivo")
    metodo_pago = int(input("Ingrese el numero del metodo de pago: "))

    if metodo_pago not in [1, 2, 3]:
        print("Opcion de metodo de pago ingresada es incorrecta por favor intente de nuevo")
        continue

    while True:
        targeta_socio = input("¿El cliente es tiene targeta de socio del supermercado? (s/n)").lower()

        if targeta_socio not in ["s", "n"]:
            print("Opcion ingresada incorrecta por favor intente de nuevo")
            continue
        else:
            break
    break




