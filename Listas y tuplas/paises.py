#Escribir un programa que enumere los países de la siguiente lista:
#paises = ['Canada', 'USA', 'Mexico', 'Australia', Argentina, China, India]

#Lista
paises = ["Canada", "USA", "Mexico", "Australia", "Argentina", "China", "India"]

#Recorrer la lista y mostrar el resultado
for indice, valor in enumerate(paises):
    print(f"[{indice} {valor}]")
    print("---------------")
