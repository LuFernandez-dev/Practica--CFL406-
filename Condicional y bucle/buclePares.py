#Crear un bucle que sume los pares del 0 al 100

#Variable acumuladora
suma_pares = 0

#Bucle para los pares
for num in range(0,101,2):
    suma_pares += num

#Resultado
print(f"El resultado de la suma es: {suma_pares}")