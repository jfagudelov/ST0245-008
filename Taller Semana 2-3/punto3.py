def invertir(s):
    if s == '':
        return s
    else:
        return invertir(s[1:]) + s[0]
