#Se tiene una cadena de texto, pero al revés. Al parecer contiene el
#nombre de un alumno, la nota de un exámen y la materia.
#se pide formatear la candena y guardas el nombre, la nota y la materia
#en distintas variables (Usar las variables para crear una oracion)

#Variables
cadena_volteada = "acitametaM ,5.8 ,otipeP ordeP"
cadena_formateada = cadena_volteada[::-1]
nombre_completo = cadena_formateada[0:12:1]
nota = cadena_formateada[14:17:1]
materia = cadena_formateada[19:29:1]

#Resultado
print(cadena_formateada)
print(nombre_completo)
print(nota)
print(materia)
print(f"El alumno {nombre_completo} tiene una nota en {materia} de {nota}")
