#Escribir un programa que le pregunte al usuario números hasta que ingrese el
#0, cuando lo haga mostrar por pantalla la suma de todos los números ingresados
#se agregaran a una lista todos los numeros ingresados (Excepto el cero)

#Valores y listas inicializadas
num = int(input("Ingrese un numero (Diferente de cero): "))
suma_num = 0
lista_num = []

#Bucle while
while num != 0:
    lista_num.append(num)
    suma_num += num
    num = int(input("Ingrese otro numero (Elija cero para terminar el bucle): "))

#Resultados
print(f"Los numeros ingresados son: ",lista_num,"\nY la suma es:", {suma_num})