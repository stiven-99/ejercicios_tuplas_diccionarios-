from carro import Carro 

class Carro_transportador(Carro):
    def __init__(self, modelo, color, motor):
        super().__init__(modelo,  color)
        self.motor = motor

    def set_datos(self, nuevo_modelo, nuevo_color, nuevo_motor):
        super().set_datos(nuevo_modelo, nuevo_color)
        self.motor = nuevo_motor

    def ver_info(self):
        info = f"INFORMACION DEL CARRO TRANSPORTADOR: \n modelo: {self.modelo} \n color: {self.color} \n motor: {self.motor}"
        return info
    
    
    
    