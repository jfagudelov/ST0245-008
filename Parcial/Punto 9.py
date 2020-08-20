def triangulo_pascal(row):
    if row == 0:
        return []
    elif row == 1:
        return [1]
    else:
        nueva_fila = [1]
        ultima_fila = triangulo_pascal(row-1)
        for i in range(len(ultima_fila)-1):
            nueva_fila.append(nueva_fila[i-1] + ultima_fila[i])
        nueva_fila += [1]
    return nueva_fila

print(triangulo_pascal(4))
