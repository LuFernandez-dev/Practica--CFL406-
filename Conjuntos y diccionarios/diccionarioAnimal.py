#Programa las siguientes instrucciones de forma ordenada sobre la variable animales:

#Añade al diccionario las claves perro, tigre y mono con sus respectivos
#valores “Bobby”, “Peepe” y “homero”. respectivamente. Muestra en
#pantalla como queda

#Modificá las claves elefante y delfin con los valores “Trompis”y “Manolo”
#respectivamente. Muestra en pantalla como queda

#Muestra los items clave y valor con un ciclo for.

#Determinar si : “perro” no pertenece al diccionario, si “mono” no pertenece
#al diccionario, si “oso” no pertenece al diccionario, “tigre” pertenece al
#diccionario

#Diccionarios
animales = {"elefante":""}
animales_nuevos = {"perro":"Bobby", "tigre":"Peepe", "mono":"Homero", "delfin":""}

#Ingresar datos al diccionario
animales.update(animales_nuevos)
print(f"Diccionario se añadio nuevos animales: \n", animales)

#Cambiar valores del diccionario
animales["elefante"] = "Trompis"
animales["delfin"] = "Manolo"
print(f"Diccionario actualizado: \n", animales)

#Mostrar el diccionario
for clave, valor in animales.items():
    print("Clave: " + clave + " Valor: " + valor) 

#Determinar si pertenecen al diccionario o no
print(f"Perro no pertenece a la lista: ", "perro" not in animales)
print(f"Mono no pertenece a la lista: ", "mono"  not in animales)
print(f"Oso no pertenece a la lista: ", "oso"   not in animales)
print(f"Tigre pertenece a la lista: ", "tigre" in animales)
