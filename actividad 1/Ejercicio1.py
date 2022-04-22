import random
print("Ejercicio 1")

def buscador(nrandom): 
  try:
    ndx = lista.index(nrandom)
  except:
    ndx = -1
  print(ndx)


while True:
  lista = [random.randint(0, 100) for x in range(7)]
  print(lista)
  nrandom= int(input("ingrese el numero q quiera buscar "))
  buscador(nrandom)
    