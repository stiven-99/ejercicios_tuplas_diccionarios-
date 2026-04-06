from plastico import Botella_plastica
from vidrio import Botella_vidrio
from base_datos import Base_datos

obj_base_datos = Base_datos()

while True:
    print("----- MENU DE OPCIONES ---- ")
    print("1. guardar una nueva botella de plastica")
    print("2. guardar una nueva botella de vidrio")
    print("3. mostrar listas de botellas")
    print("4. modificar una botella")
    print("5. eliminar una posicion de botella")
    print("6. salir del menu")

    opcion = input("selecciona una opcion: ")

    if opcion == "1":
        material = input("ingrese el material: ")
        capacidad = input("ingrese la cantidad: ")
        forma = input("ingrese la forma: ")

        obj_botella = Botella_plastica(material, capacidad, forma)
        obj_base_datos.agregar_botella(obj_botella)

    if opcion == "2":
        material = input("ingrese el material: ")
        capacidad = input("ingrese la cantidad: ")
        forma = input("ingrese la forma: ")

        obj_botella = Botella_vidrio(material, capacidad, forma)
        obj_base_datos.agregar_botella(obj_botella)

    elif opcion == "3":
        print("\n ---- BOTELLAS REGISTRADAS ----")
        for i in range(len(obj_base_datos.lista_botella)):
            print(f"[{i}] {obj_base_datos.lista_botella[i].ver_info()}")

    elif opcion == "4":
        index = int(input("posicion a modificar: ")) 
        material = input("nuevo material: ")
        capacidad = input("nueva capacidad: ")
        forma = input("nueva forma: ")
        obj_base_datos.modificar_botella(index, material, capacidad, forma)

    elif opcion == "5":
        index = int(input("posicion a eliminar: "))
        obj_base_datos.eliminar_botella(index)

    elif opcion == "6":
        print("saliendo del sistema")
        break

