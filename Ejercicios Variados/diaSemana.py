#Se debe desarrollar un programa en el que se ingrese un número de 1 a 7 e informe a qué día
#de la semana equivale. Ejemplo 2 = “Martes”.

#Ingreso de datos y diccionario
num_dia = int(input("Ingrese un numero del dia correspondiente (1 Lunes a 7 Domingo): "))
semana = {1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado", 7:"Domingo"}

#Verificacion y resultado
if num_dia in semana:
    print(f"El dia de la semana es:", semana[num_dia])
else:
    print("Numero ingresado incorrecto")