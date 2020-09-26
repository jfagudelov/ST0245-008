import random as rd

def quick_sort(lista):
    derecha = []
    izquierda = []
    centro = []
    if len(lista) > 1:
        pivote = lista[len(lista)-1]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista

lista_a = []
lista_b = []
for i in range(1,51):
  lista_a.append(rd.randint(-10, 101))
  lista_b.append(rd.randint(1, 101))
lista_mix = lista_a + lista_b
print('lista A:', quick_sort(lista_a))
print('lista B:', quick_sort(lista_b))
print('lista A+B:', quick_sort(lista_mix))
