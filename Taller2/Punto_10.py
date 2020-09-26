# La función pasa por cada fila de la matriz y verifica si su primer o último elemento es igual a la llave. En caso contrario,
# verifica si el último elemento es mayor a la llave y si el primer elemento es menor a la llave.

# Ya que la lista está organizada, hacer estas verificaciones nos permite encontrar más rápido la fila dónde se encuentra
# el elemento.

def encontrar_elemento(matriz, llave):
  encontrado = False
  for fila in matriz:
    if fila[0] == llave or fila[len(fila)-1] == llave:
        encontrado = True
        break
    elif fila[len(fila)-1] >= llave and fila[0] <= llave:
      if llave in fila:
        encontrado = True
        break
      else:
        encontrado = False
  return encontrado

matriz = [[1,2,2,2], [1,2], [3,4,4], [4,5,6,7,8,9]]
print(encontrar_elemento(matriz, 1))
