from caballo import Caballo
from cocodrilo import Cocodrilo
from cucarron import Cucarron
from pato import Pato
from pez import Pez
from base_datos import Base_datos

obj_base_datos = Base_datos()

while True:
    print("---- MENU DE ANIMALES ----")
    print("1. agregar el animal caballo ")
    print("2. agregar el animal cocodrilo")
    print("3. agregar el animal cucarron")
    print("4. agregar el animal pato")
    print("5. agregar el animal pez")
    print("6. ver lista de animales agregados")
    print("7. modificar un animal segun la posicion")
    print("8. eliminar un animal segun la posicion")
    print("9. salir del menu")
    
    opcion = input("seleccion una opcion: ")
    
    if opcion == "1":
        nombre = input("ingrese el nombre del caballo: ")
        edad = input("ingrese la edad del caballo: ")
        habitat = input("ingrese el habbitat del caballo: ")
        color = input("ingrese el color del caballo: ")
        obj_animal = Caballo(nombre, edad, habitat, color)
        obj_base_datos.agregar_animal(obj_animal)
        
    if opcion == "2":
        nombre = input("ingrese el nombre del cocodrilo: ")
        edad = input("ingrese la edad del cocodrilo: ")
        habitat = input("ingrese el habbitat del cocodrilo: ")
        color = input("ingrese el color del cocodrilo: ")
        obj_animal = Cocodrilo(nombre, edad, habitat, color)
        obj_base_datos.agregar_animal(obj_animal)
        
    if opcion == "3":
        nombre = input("ingrese el nombre del cucarron: ")
        edad = input("ingrese la edad del cucarron: ")
        habitat = input("ingrese el habbitat del cucarron: ")
        color = input("ingrese el color del cucarron: ")
        obj_animal = Cucarron(nombre, edad, habitat, color)
        obj_base_datos.agregar_animal(obj_animal)
        
    if opcion == "4":
        nombre = input("ingrese el nombre del pato: ")
        edad = input("ingrese la edad del pato: ")
        habitat = input("ingrese el habbitat del pato: ")
        color = input("ingrese el color del pato: ")
        obj_animal = Pato(nombre, edad, habitat, color)
        obj_base_datos.agregar_animal(obj_animal)
        
    if opcion == "5":
        nombre = input("ingrese el nombre del pez: ")
        edad = input("ingrese la edad del pez: ")
        habitat = input("ingrese el habbitat del pez: ")
        color = input("ingrese el color del pez: ")
        obj_animal = Pez(nombre, edad, habitat, color)
        obj_base_datos.agregar_animal(obj_animal)
        
    elif opcion == "6":
        print("\n ----- ANIMALES REGISTRADOS -----")
        for i in range(len(obj_base_datos.lista_animales)):
            print(f"[{i}] {obj_base_datos.lista_animales[i].ver_info()}")
            
    elif opcion == "7":
        index = int(input("posicion a modificar: "))
        nombre = input("ingrese el nuevo nombre del animal: ")
        edad = input("ingrese la nueva edad del animal: ")
        habitat = input("ingrese la nueva habitat del animal: ")
        color = input("ingrese el nuevo color del animal: ")
        obj_base_datos.modificar_animal(index, nombre, edad, habitat, color)
        
    elif opcion == "8":
        index = int(input("posicion a eliminar: "))
        obj_base_datos.eliminar_animal(index)
        
    elif opcion == "9":
        print("saliendo del menu")
        break
    