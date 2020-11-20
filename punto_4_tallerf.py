#Ejercicio pollo pollo 
n= int(input("Escriba nuemero de pollo que desea\n"))
def compar_pollo(n):
    a = 6
    b = 9
    c = 20
    d = a+b
    val1 = n//a
    val2 = n//b
    val3 = n//(a+b)
    val4 = n//c

    if n%a == 0:
        if n%b == 0:
            print("puede comprar ",val1, " bolasas de", a, " pollos")
            print("tambien puedes comrar ",val2, " bolsas de ", b, " pollos")
        elif n%c == 0:
            print("puede comprar ",val1, " bolasas de", a, " pollos")
            print(" tambien puede comprar ", val4, " bolsas de ",c," pollos")
        elif n%b==0 and n%c==0:
            print("puede comprar pollos de a 6, de a 9 y de a 20")
        else:
            print("puede comprar ", n//a, " bolsas de ", a, " pollos")

    elif n%d==0:
            print("puedes comprar " ,val3, " bolsas de ", a, " y ", val3, "bolsas de", b )

    elif n%c == 0:
        print("puedes comprar ", n//c, " bolsas de ", c, " pollos")

    elif n%b == 6:
        print("puedes comprar ", 1, " bolsas de ", a ," pollos y ", (n-(n%9))//9, " bolsas de pollos de ", b )

    elif n%b == 0:
        print("puedes comprar ", n//9, " boslas de ", b, " pollos ")

    else:
        print("No se puede comprar esta cantidad")

print(compar_pollo(n))
