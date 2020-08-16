def hanoi (n,p_inicial,p_final,p_auxiliar):
    if n == 1:
        print("Pasa el disco de la posicion: " + p_inicial+","+" a la posicion: "+p_final)
    else:
        hanoi(n-1,p_inicial,p_auxiliar,p_final)
        print("Pasa del disco de la posicion: "+p_inicial+","+" a la posicion: "+p_final)
        hanoi(n-1,p_auxiliar,p_final,p_inicial)
