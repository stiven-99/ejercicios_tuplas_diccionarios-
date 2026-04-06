from carro_deportivo import Carro_deportivo
from carro_pesado import Carro_pesado
from carro_transportador import Carro_transportador
from base_datos import Base_datos

obj_base_datos = Base_datos()

while True: 
    print(" ----- MENU DE CARROS ----")
    print("1. agregar carro deportivo")
    print("2. agregar carro pesado")
    print("3. agregar carro de transporte")
    print("4. ver lista de carros agregados")
    print("5. modificar carro segun la posicion")
    print("6. eliminar carro segun la posicion")
    print("7. salir del menu")

    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        modelo = input("ingrese el modelo del carro: ")
        color = input("ingrese el color del carro: ")
        motor = input("ingrese el motor del carro: ")
        obj_carro = Carro_deportivo(modelo, color, motor)
        obj_base_datos.agregar_carro(obj_carro)

    if opcion == "2":
        modelo = input("ingrese el modelo del carro: ")
        color = input("ingrese el color del carro: ")
        motor = input("ingrese el motor del carro: ")
        obj_carro = Carro_pesado(modelo, color, motor)
        obj_base_datos.agregar_carro(obj_carro)

    if opcion == "3":
        modelo = input("ingrese el modelo del carro: ")
        color = input("ingrese el color del carro: ")
        motor = input("ingrese el motor del carro: ")
        obj_carro = Carro_transportador(modelo, color, motor)
        obj_base_datos.agregar_carro(obj_carro)

    elif opcion == "4":
        print("\n ----- BOTELLAS REGISTRADAS ----- ")
        for i in range(len(obj_base_datos.lista_carros)):
            print(f"[{i}] {obj_base_datos.lista_carros[i].ver_info()}")

    elif opcion == "5":
        index = int(input("posicion a modificar: "))
        modelo = input("ingrese el  nuevo modelo del carro: ")
        color = input("ingrese el nuevo color del carro: ")
        motor = input("ingrese el nuevo motor del carro: ")
        obj_base_datos.modificar_carro(index, modelo, color, motor)

    elif opcion == "6":
        index = int(input("posicion a eliminar: "))
        obj_base_datos.eliminar_carro(index)

    elif opcion == "7":
        print("saliendo del menu")
        break