#Dado sueldo y antigüedad, incrementar el sueldo en un 25% si la antigüedad es mayor a 15 años; si es
#menor a 15 años mostrar en pantalla el sueldo del empleado. Diseñe un programa
#correspondiente, informando el sueldo final.

#Ingreso de datos
salario = float(input("Ingrese su salario: "))
antiguedad = int(input("Ingrese sus años trabajado: "))

#Verificacion de datos
if antiguedad > 15:
    salario_total = salario + (salario * 0.25)
else:
    salario_total = salario

#Mostrar resultados
print(f"Salario final del empleado: {round(salario_total, 2)}\nAntigüedad del empleado: {antiguedad}")