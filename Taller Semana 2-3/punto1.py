n = int(input("Ingrese el primer numero \n"))
m = int(input("Ingrese el segundo numero \n"))

def mcd (n,m):
    mod = n%m
    mod2 = m%n
    if n>m:
        if mod == 0:
            return m
        else:
            x = m
            y = mod
            return mcd(x,y)
    elif m>n:
        if mod2 == 0:
            return n
        else:
            x = m
            y = mod
            return mcd(x,y)
print(mcd(n,m))
