#Crea una clase llamada Tarea que represente una tarea en una lista de pendientes. Cada tarea debe tener:
#titulo, descripcion y entregado
#Debe tener las funciones marcar_completado() y mostrar_info()
#Crea una clase gestionTarea que tendra una lista de tarea y los metodos
#agregar_tarea(), mostrar_todas() y mostrar_pendientes()

class Tarea:

    #Constructor de la clase Tarea
    def __init__(self, titulo, descripcion, completada = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada
    
    #Metodo para marcar la tarea como completado
    def marcar_completado(self):
        self.completada = True
    
    #Metodo que muestra la informacion de una tarea y dice si esta completada o pendiente
    def mostrar_info(self):
        estado = "Completado" if self.completada else "Pendiente"

        print(f"Titulo: {self.titulo}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Estado: {estado}")
        print("-" * 30)

class GestionTarea:

    #Constructor de la clase GestionTarea
    def __init__(self):
        self.lista_tarea = []
    
    #Metodo para agregar tareas a una lista
    def agregar_Tarea(self, tarea):
        self.lista_tarea.append(tarea)
    
    #Muestra todas las tareas 
    def mostrar_todas(self):
        for tarea in self.lista_tarea:
            tarea.mostrar_info() 

    #Muestra las tareas pendientes
    def mostrar_pendiente(self):
        for tarea in self.lista_tarea:
            if not tarea.completada:
                tarea.mostrar_info()

#main
t1 = Tarea("Estudiar Python", "Repasar clases y objetos")
t2 = Tarea("Hacer ejercicio", "30 minutos de caminata")

#t1.mostrar_info()
t1.marcar_completado()
#t1.mostrar_info()

gestion = GestionTarea()

gestion.agregar_Tarea(t1)
gestion.agregar_Tarea(t2)

#gestion.mostrar_todas()

gestion.mostrar_pendiente()



