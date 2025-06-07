#Programa que pida el ingreso de una letra y diga si es vocal o no
#Incluso si es mayuscula o con acento

#Ingreso de datos
letra = input("Ingrese una letra: ").lower()

#Lista de vocales
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

#Verificacion de la letra y resultado
if len(letra) != 1:
    print("Ingrese solo una letra")
elif letra in vocales:
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")

