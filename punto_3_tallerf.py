def postorden(pre, ino):
    #Se revisa si la cadena esta vacia, para retornar la cadena de postorder vacia
    if pre == "":
        return ""
    #Si la cadena tiene un caracter, por lo tanto el post order va a ser ese mismo caracter
    if len(pre)==1:
        return pre
    PostOrden = ""
    Ino_izq = ""
    Pre_izq = ""
    Ino_der = ""
    Pre_der = ""
    aux = 0
    #ciclo while para verificar que el caractar en una posicion del preorder sea diferente al del inorder
    while ino[aux] != pre[0]:
        Ino_izq = Ino_izq + ino[aux]
        aux+=1
    aux+=1

    while aux<len(ino):
        Ino_der = Ino_der + ino[aux]
        aux+=1
    aux=0
    #ciclo para añadir a la cadena de postorder, los caracteres en el orden que deben estar
    for i in pre:
        if i in Ino_izq:
            Pre_izq = Pre_izq + i
        if i in Ino_der:
            Pre_der = Pre_der + i
    PostOrden = PostOrden+postorden(Pre_izq, Ino_izq)+postorden(Pre_der, Ino_der)+pre[0]
    return PostOrden
print(postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))
