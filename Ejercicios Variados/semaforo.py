#Diseñe un programa que simula un semáforo, y el dato de entrada son los
#colores (Verde, Amarrillo, Rojo).

#Ingreso de datos
color = input("Ingrese un color (verde, amarillo o rojo): ").lower()

#Verificacion y resultado
if color == "verde":
    print("Avancen")
elif color == "amarillo":
    print("Precaucion")
elif color == "rojo":
    print("Detenerse")
else:
    print("Color ingresado invalido")