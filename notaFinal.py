#Programa que calcula la nota final del alumno pasandole la
#nota de los dos primero examen junto con el nombre completo
#del alumno.

#Ingreso de datos
nombre_completo = input("Ingrese su nombre junto con el apellido separado por el espacio: ")
nota_1 = float(input("Ingrese la nota del primer examen: "))
nota_2 = float(input("Ingrese la nota del segundo examen: "))

#Variables
porcen_nota_1 = 0.5
porcen_nota_2 = 0.3
nota_final = (porcen_nota_1 * nota_1 + porcen_nota_2 * nota_2) / (porcen_nota_1 + porcen_nota_2)

#Resultado
print(f"el alumno {nombre_completo} tiene una nota final de: ", round(nota_final, 1))






