from animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, color):
        super().__init__(nombre, edad, habitat)
        self.color = color
        
    def set_datos(self, nuevo_nombre, nueva_edad, nueva_habitat, nuevo_color):
        super().__init__(nuevo_nombre, nueva_edad, nueva_habitat)
        self.color = nuevo_color
        
    def ver_info(self):
        info = f"INFORMACION DEL ANIMAL COCODRILO: \n nombre: {self.nombre} \n edad: {self.edad} \n  habitat: {self.habitat} \n color: {self.color}"
        return info 
        