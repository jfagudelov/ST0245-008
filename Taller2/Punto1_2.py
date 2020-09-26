# La función cuenta las ocurrencias de cada elemento de la lista. Si sus ocurrencias son mayores a 1, entonces borra las primeras ocurrencias.

def eliminar_repetidos(lista):
  for elemento in lista:
    contador = lista.count(elemento)
    if contador > 1:
      lista.remove(elemento)
  return lista

lista = [4,7,11,4,9,5,11,7,3,5]
lista_ordenada = [1,2,2,3,3,3,4,5,6]
print(eliminar_repetidos(lista_ordenada))
