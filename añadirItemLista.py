#Añade a la LISTA1 el int 1234 y luego el string “Hola”
#Añade a la LISTA2 el string “Adios” y luego el int 1234
#Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
#Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
#Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

#Listas
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]
lista3 = lista1[0:2:1]
lista4 = lista2[1:3:1]
lista5 = lista4 + lista3

#Agremamos item
lista1.append(1234)
lista2.append("Adios")
lista2.append(1234)

#Resultado
print(lista1) 
print(lista2)
print(lista3)
print(lista4)
print(lista5)
