def triangulo_pascal(k):
    if k == 0:
        return []
    elif k == 1:
        return [1]
    else:
        nueva_fila = [1]
        ultima_fila = triangulo_pascal(k-1)
        for i in range(len(ultima_fila)-1):
            nueva_fila.append(nueva_fila[i] + ultima_fila[i+1])
        nueva_fila += [1]
    return nueva_fila
