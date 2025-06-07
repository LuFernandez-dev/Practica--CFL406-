#Escribir un programa que le pregunte al usuario su edad y muestre por
#pantalla si es mayor de edad o no.

#Ingreso de datos
edad = int(input("ingrese la edad del usuario: "))

#Verificacion y resultado
if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")