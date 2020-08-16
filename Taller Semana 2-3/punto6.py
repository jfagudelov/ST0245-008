def fibonacci(k):
    if k<0:
        print('Valor debe ser mayor a 0!')
    elif k == 1:
        return 0
    elif k == 2:
        return 1
    else:
        return fibonacci(k-1)+fibonacci(k-2)
