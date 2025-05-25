#averiguar la longitud(len) de  texto_1 y texto_2 (en archivos .py se escribe asi: print(len(texto_1))) 
#averiguar de texto_2 que letra esta en el indice [2] y [5], imprimiendolos en pantalla asi: print(cadena_2[2]) 
#averiguar de texto_1 que indice inverso tiene en [-2] y [-5], imprimiendolos en pantalla asi: print(cadena_2[-2])

#Ingreso de datos
texto_1 = input("Ingrese unas palabras: ")
texto_2 = input("Ingrese otras palabras: ")

#Resultado
print(f" El numero de cararteres de texto 1 es: {len(texto_1)} \n El numero de cararteres de texto 2 es: {len(texto_2)}")

#Indice de texto 1 y 2
if len(texto_1) >= 5 and len(texto_2) >= 5:
    print(f"La letra de indice -2 es: {texto_1[-2]}")
    print(f"La letra de indice -5 es: {texto_1[-5]}")
    print(f"La letra de indice 2 es: {texto_2[2]}")
    print(f"La letra de indice 5 es: {texto_2[5]}")
else:
    print("Los textos deben tener minimo 5 cararteres")