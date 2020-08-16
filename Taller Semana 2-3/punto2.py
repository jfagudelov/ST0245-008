def potencia(j, k):
    if k == 0:
        return 1
    else:
        return j*potencia(j,k-1)
