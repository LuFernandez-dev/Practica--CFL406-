#Diseñe un programa, para ayudar a un cajero de
#supermercado, si el cliente tiene la tarjeta de socio en cada compra se le hace un 20% de descuento. Si
#paga con tarjeta de crédito se le aplica un recargo del 15%. Y si paga con tarjeta de débito o efectivo se
#le hace un 15% de descuento.

#Ingreso del total de pago
total_sin_decuento = float(input("Ingrese el total de la compra: "))

#Guardar el total sin descuento
total_final = total_sin_decuento

#Bucle para la verificacion de los datos introducidos 
while True:
    print("1.Credito\n2.Debito\n3.Efectivo")
    metodo_pago = int(input("Ingrese el numero del metodo de pago: "))

    if metodo_pago not in [1, 2, 3]:
        print("\nOpcion de metodo de pago ingresada es incorrecta por favor intente de nuevo...\n")
        continue #Si se ingresa una opcion incorrecta vuelve a preguntar

    while True:
        targeta_socio = input("\n¿El cliente es tiene targeta de socio del supermercado? (s/n):").lower()

        if targeta_socio not in ["s", "n"]:
            print("\nOpcion ingresada incorrecta por favor intente de nuevo...")
            continue #Si se ingresa una opcion incorrecta vuelve a preguntar
        else:
            break #Sale del bucle de la verificacion de caracteres correctos (Targeta de socio)

    break #Sale del bucle de la verificacion de caracteres correctos (Metodo de pago)

#Si se entra agrega el descuento de socio
if targeta_socio == "s":
    total_final *= 0.80

#Dependiendo del metodo se hara un recargo o un decuento
if metodo_pago == 1:
    total_final *= 1.15
elif metodo_pago == 2 or metodo_pago == 3:
    total_final *= 0.85

#Muestra el resultado
print(f"\nEl precio total sin decuento es: {round(total_sin_decuento, 2)}\nY el precio con descuento y/o recargo es: {round(total_final, 2)}")