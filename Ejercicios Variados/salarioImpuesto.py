#Diseñe programa donde se está solicitando el salario mensual
#de un trabajador indique si paga o no determinado impuesto. Si el salario es mayor a 15000 informar
#"Se retienen impuestos", en caso contrario "No alcanzado por el impuesto".

#Ingreso de datos
salario = float(input("Ingrese su salario: "))

#Verificacion y resultado
if salario > 15000:
    print("Se retienen impuestos\nSalario: ", salario)
else:
    print("No alcanzado por el impuesto\nSalario: ", salario)