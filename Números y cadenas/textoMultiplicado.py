#Ingresar por teclado dos cadenas de texto a las cuales vamos a llamar texto_1 y texto_2 
#(ingresar las palabras que quieran) 
#y concatenarlas, luego multiplicar cada una *2
#imprimir en pantalla  los resultados

#Ingreso de datos
texto_1 = input("Ingrese unas palabras: ")
texto_2 = input("Ingrese otras palabras: ")

#Variable
texto_unido = (texto_1 + " " + texto_2)
texto_1_m = texto_1 * 2 
texto_2_m = texto_2 * 2

#Resultado
print(f" Texto unido: {texto_unido} \n texto multiplicado: {texto_1_m}  {texto_2_m}")
