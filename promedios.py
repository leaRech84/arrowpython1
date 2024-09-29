active = True

while active == True:
  print("Ingrese su primer nota")
  primer_nota = float(input("Primer nota: "))
  
  print("Ingrese su segunda nota")
  segunda_nota = float(input("Segunda nota: "))
 
  print("Ingrese su tercer nota")
  tercer_nota = float(input("Tercer nota: "))
  
  active = False
  promedio = (primer_nota + segunda_nota + tercer_nota) / 3
  print(f"El promedio es {promedio}")