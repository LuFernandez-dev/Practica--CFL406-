#Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#1.Mostrar una suma de los dos números 
#2.Mostrar una resta de los dos números (el primero menos el segundo) 
#3.Mostrar una multiplicación de los dos números 
#4.Si elige esta opción(opcion 4) se interrumpirá la impresión del menú y el programa finalizará 
#5.En caso de no introducir una opción válida, el programa informará de que no es correcta.

#Importaciones
import os

#Ingreso de datos
num_a = int(input("Ingrese un numero: "))
num_b = int(input("Ingrese otro numero: "))

#Bucle while para la calculadora
while True:
    #Opciones
    print("----------> CALCULADORA <----------\n")
    print("1.SUMAR")
    print("2.RESTAR")
    print("3.MULTIPLICAR")
    print("4.DIVIDIR")
    print("5.SALIR\n")
    option = int(input("Ingrese el numero de la opcion: "))
    os.system("cls") #Limpia la pantalla

    #Operaciones
    try:
        if option == 1:
            print(f"La suma de los numeros es: {num_a} + {num_b} = {num_a + num_b}\n") #Suma
        elif option == 2:
            print(f"La resta de los numeros es: {num_a} - {num_b} = {num_a - num_b}\n") #Resta
        elif option == 3:
            print(f"La multiplicacion de los numeros es: {num_a} * {num_b} = {num_a * num_b}\n") #Multiplicacion
        elif option == 4:
            print(f"La division de los numeros es: {num_a} / {num_b} = {num_a / num_b}\n") #Division
        elif option == 5:
            print("Fin del programa\n") 
            break #Sale del bucle
        else:
            print("Opcion ingresada invalida intente de nuevo...") #Error en las opciones de la calculadora
    except Exception as e:
        print("Ha ocurrido un error", type(e).__name__) #Identifica errores no previsto
