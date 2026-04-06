class Carro:
    def __init__(self, modelo, color):
        self.modelo = modelo
        self.color = color

    def get_modelo(self):
        return self.modelo
    
    def get_color(self):
        return self.color
    
    def set_datos(self, nuevo_modelo, nuevo_color):
        self.modelo = nuevo_modelo
        self.color = nuevo_color

    def ver_info(self):
        info = f"modelo: {self.modelo}"
        info = info + f"color: {self.color}"
        return info
    
    