#Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:
#Añade los usuarios: Ana, Ramón, Marta, Eric, David,Esteban
#Elimina los usuarios: Mario, Miguel, Esteban

#Conjuntos
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
nuevos_usuarios = {"Ana", "Ramón", "Marta", "Eric", "David", "Esteban"}
eliminados = {"Mario", "Miguel", "Esteban"}

#Agregar usuarios 
grupo.update(nuevos_usuarios)
print(f"Usuarios nuevos agregados:\n", grupo)

#Remover usuarios
for i in eliminados:
    grupo.discard(i)

#Resultado
print(f"Conjunto de usuarios actualizado:\n", grupo)


#Otra solucion

#Agregar usuarios
#grupo.update(["Ana", "Ramón", "Marta", "Eric", "David","Esteban"])
#print(f"Usuarios nuevos agregados:\n", grupo)

#Remover usuarios
#grupo.remove("Mario")
#grupo.remove("Miguel")
#grupo.remove("Esteban")
#print(f"Conjunto de usuarios actualizado:\n", grupo)
