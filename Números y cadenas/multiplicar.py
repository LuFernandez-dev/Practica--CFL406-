#2.Ingresar por teclado dos numeros con coma(float), y en una nueva variable llamada respuesta_2 
#guardar la multiplicación de los dos numeros.
#imprimir en pantalla en la pantalla el resultado  de los numeros almacenados en "respuesta_2" 
#Ayuda: usamos f-string.

#Ingreso de datos
num_1 = float(input("Ingrese un numero: "))
num_2 = float(input("Ingrese otro numero: "))

#variable
respuesta_2 = num_1 * num_2

#Resultado
print(f" El resultado de la multiplicacion es: {round(respuesta_2, 2)}")
