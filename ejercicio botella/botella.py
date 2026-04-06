class Botella:
    def __init__(self, material, capacidad):
        self.material = material
        self.capacidad = capacidad

    def get_material(self):
        return self.material
    
    def get_capacidad(self):
        return self.capacidad

    def set_datos(self, nuevo_material, nueva_capacidad):
        self.material = nuevo_material
        self.capacidad = nueva_capacidad

    def ver_info(self):
        pass 