#Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
#Por ejemplo, si el número es 75869, la salida debería ser 5

#Variable
num = int(input("Ingrese un numero: "))

#Contador de digitos
print(f"La cantidad de digitos que tiene es: {len(str(num))}")