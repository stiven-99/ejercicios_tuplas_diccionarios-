class Animal:
    def __init__(self, nombre, edad, habitat):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_habitat(self):
        return  self.habitat
    
    def set_datos(self, nuevo_nombre, nueva_edad, nueva_habitat):
        self.nombre = nuevo_nombre
        self.edad = nueva_edad
        self.habitat = nueva_habitat
        
    def ver_info(self):
        info = f"nombre: {self.nombre} \n edad: {self.edad} \n habitat: {self.habitat}"
        return info
    