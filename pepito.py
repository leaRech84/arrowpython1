pedido = []

active = True



while active == True:
    print("Menu: 1): Hamburguesa de cheddar | 2): Gaseosa | 3): Agua Mineral | 4): Papas Fritas | 5) Sandwich de milanesa | 6) Finalizar pedido")
    opcion = int(input("Ingresa la opción: ")) 
    
    if opcion == 1:
      pedido.append("Hamburguesa de cheddar")
      print(pedido)
    elif opcion == 2:
      pedido.append("Gaseosa")
      print(pedido)
    elif opcion == 3:
      pedido.append("Agua Mineral")
      print(pedido)
    elif opcion == 4:
      pedido.append("Papas fritas")
      print(pedido)
    elif opcion == 5:
      pedido.append("Sandwich de milanga")
      print(pedido)
    else:
      active = False     
      print("Te esperamos cuando gustes")
      
      
promedio = []

while active == True:
  print("Ingrese su primer nota")
  primer_nota = float(input("Primer nota: "))
  promedio.append(float(primer_nota))


  print("Ingrese su segunda nota")
  segunda_nota = float(input("Segunda nota: "))
  promedio.append(float(segunda_nota))

  print("Ingrese su tercer nota")
  tercer_nota = float(input("Tercer nota: "))
  promedio.append(float(tercer_nota))