#Confeccionar un programa que determine si un número leído por teclado se
#encuentra en el intervalo [2, 90].

#Ingreso de datos
num = int(input("Ingrese un numero: "))

#Verificacion y resultado
if num >= 2 and num <= 90:
    print("El numero se encuentra en el intervalo")
else:
    print("El numero no se encuentra en el intervalo")