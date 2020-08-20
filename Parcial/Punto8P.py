def numeros_descendientes(n):
    if n == 0:
        return 0
    else:
        print(n)
        return numeros_descendientes(n-1)
    
print(numeros_descendientes(20))
