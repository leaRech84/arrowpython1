created_shoes = []

class SoccerShoes():
  def __init__(self, idn, brand, price, size, colour):
    self.id = idn
    self.brand = brand
    self.price = price
    self.size = size
    self.colour = colour

  def change_size(self, new_size):
    self.size = new_size
  
  def __str__(self):
        return f"ID: {self.id}, Marca: {self.brand}, Precio: {self.price}, Talle: {self.size}, Color: {self.colour}"

id = 1

#Functions
def create_shoes(param_id):
  brand = input("Ingrese la marca de los botines: ")
  price = int(input("Ingrese el precio de los botines: "))
  size = int(input("Ingrese el talle de los botines: "))
  colour = input("Ingrese el color de los botines: ")
  shoes = SoccerShoes(param_id, brand, price, size, colour)
  created_shoes.append(shoes)
  print(f"Botines creados exitosamente: {shoes}")

def delete_shoes():
  select_id = int(input("Ingrese el ID de los botines que quiere eliminar: "))
  for shoes in created_shoes:
    if shoes.id == select_id:
      created_shoes.remove(shoes)
      print(f"Botines con ID {select_id} eliminados.")
      return
    print("Error: No se encontró un botín con ese ID.")
    
def update_size():
    select_id = int(input("Ingrese el ID de los botines que quiere actualizar: "))
    for shoes in created_shoes:
        if shoes.id == select_id:
          new_size = int(input(f"Ingrese el nuevo talle para los botines (actual: {shoes.size}): "))
          shoes.change_size(new_size)
          print(f"Talle actualizado: {shoes}")
          return
    print("Error: No se encontró un botín con ese ID.")
      
def show_list():
    if created_shoes:
        print("Lista de botines:")
        for shoes in created_shoes:
            print(shoes)
    else:
        print("No hay botines creados.")


def menu():
    active = True
    id_counter = 1
    while active:
        print("\nMenú: 1) Crear Botines | 2) Eliminar Botines | 3) Actualizar Talle | 4) Mostrar Lista de Botines | 5) Salir")
        option = int(input("Ingresa la opción: "))
        if option == 1:
          create_shoes(id_counter)
          id_counter += 1
        elif option == 2:
          delete_shoes()
        elif option == 3:
          update_size()
        elif option == 4:
          show_list()
        elif option == 5:
          print("Saliendo del programa...")
          active = False
        else:
          print("Opción no válida, intenta de nuevo.")
          
#Iniciar menú
menu()
