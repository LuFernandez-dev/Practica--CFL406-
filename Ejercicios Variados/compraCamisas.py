#Diseñe programa que calcule el total a pagar por la compra de camisas. Si
#se compran 3 camisas o más, se aplica un descuento del 20% sobre el total de la compra, y si son menos
#de tres camisas un descuento del 10%.

#Ingreso de datos
cantidad_camisa = int(input("Ingrese el numero de camisas compradas: "))
precio_camisa = float(input("Ingrese el precio total por las camisas: "))

#Suma de datos y guardado en una variable
total_sin_descuento = precio_camisa * cantidad_camisa

#Verificacion del descuento y precios
if cantidad_camisa >= 3:
    descuento = 0.2
elif cantidad_camisa < 3 and cantidad_camisa >= 1:
    descuento = 0.1
else:
    print("Ingrese un numero valido") #Excepcion

if precio_camisa > 0:
    precio_descuento = total_sin_descuento * descuento
    total_con_descuento = total_sin_descuento - precio_descuento
else:
    print("Ingrese un precio valido")

#Mostrar precios
print(f"Precio sin el descuento: ", round(total_sin_descuento, 2))
print(f"Descuento: ", round(precio_descuento, 2))
print(f"Precio con el descuento: ", round(total_con_descuento, 2))
