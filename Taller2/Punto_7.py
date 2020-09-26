numeros = []
for i in range(1,51):
  numeros.append(rd.randint(-10,20))

def sacar_negativos(lista):
  lista_negativos = []
  for numero in lista:
    if numero < 0:
      lista_negativos.append(numero)
  return lista_negativos

print(sacar_negativos(numeros))
