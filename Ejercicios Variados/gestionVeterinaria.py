#Crea la clase Mascota con los siguientes atributos:
#nombre, especie, edad, y peso
#implementar los siguiente metodos:
#mostrar_info(), actualizar_peso(nuevo_peso) y necesita_revision()


class Mascota:

    #Constructor de la clase mascota
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
    
    #Metodo para mostrar la informacion de las mascota
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"¿Necesita revisión?: {self.necesita_revision()}") #Aca se vera el resultado del metodo necesita_revision()
        print("-" * 30)
    
    #Metodo para actualizar el peso de las mascotas
    def actualizar_peso(self, nuevo_peso):
        self.peso = nuevo_peso
    
    #Metodo para saber si el animal nesecita revision
    def necesita_revision(self):
        return "Si" if self.edad > 10 or self.peso < 2.0 else "No"

#Main
m1 = Mascota("Luna", "Gato", 12, 1.8)
m2 = Mascota("Ivy", "Gato", 4, 8.5)
m3 = Mascota("Nieve", "Perro", 5, 9.0)

m1.mostrar_info()
m2.mostrar_info()
m3.mostrar_info()

m3.actualizar_peso(9.2)

m3.mostrar_info()
