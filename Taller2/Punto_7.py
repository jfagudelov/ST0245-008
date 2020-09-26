import random as rd

# Se crea una lista de 50 numeros aleatorios entre -10 y 20.

numeros = []
for i in range(1,51):
  numeros.append(rd.randint(-10,20))

# Se recorre cada elemento de la lista. Si el elemento es menor a 0, entonces lo agregamos a 
# una lista con todos los negativos. Al final se retorna esta lista.
  
def sacar_negativos(lista):
  lista_negativos = []
  for numero in lista:
    if numero < 0:
      lista_negativos.append(numero)
  return lista_negativos

print(sacar_negativos(numeros))
