class Base_datos:
    def __init__(self):
        self.lista_animales = []
        
    def agregar_animal(self, nuevo_obj):
        self.lista_animales.append(nuevo_obj)
        print("animal guardado exitosamente")
        
    def eliminar_animal(self, posicion):
        for i in range(len(self.lista_animales)):
            if i == posicion:
                self.lista_animales.pop(posicion)
                print(f"animal en posicion {i} eliminado")
                break
            else: 
                print("posicion no encontrada")
                
    def modificar_animal(self, posicion, nuevo_nombre, nueva_edad, nueva_habitat, nuevo_color):
        for i in range(len(self.lista_animales)):
            if i == posicion:
                self.lista_animales[i].set_datos(nuevo_nombre, nueva_edad, nueva_habitat, nuevo_color)
                print(f"animal en posicion {i} actualizada")
                break
            else:
                print("posicion no encontrada")