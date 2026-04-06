class Base_datos:
    def __init__(self):
        self.lista_carros = []

    def agregar_carro(self, nuevo_obj):
        self.lista_carros.append(nuevo_obj)
        print("carro guardado exitosamente")

    def eliminar_carro(self, posicion):
        for i in range(len(self.lista_carros)):
            if i == posicion:
                self.lista_carros.pop(posicion)
                print(f"carro en posicion {i} eliminado")
                break
            else:
                print("posicion no encontrada")

    def modificar_carro(self, posicion, nuevo_modelo, nuevo_color, nuevo_motor):
        for i in range(len(self.lista_carros)):
            if i == posicion:
                self.lista_carros[i].set_datos(nuevo_modelo, nuevo_color, nuevo_motor)
                print(f"carro en posicion {i} actualizada")
                break
            else:
                print("posicion no encontrada")
                
