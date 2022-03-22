# n-ty wyraz ciągu
def wyrn(a1, q, n):
    an = a1 * (q ** (n-1))
    return an
def wyrnv(ak, q, n, k):
    an = ak * (q ** (n-k))
    return an

# suma n wyrazow ciągu
def sum(a1, q, n):
    if q != 1:
        sn = a1 * ((1 - q ** n)/(1 - q))
    else:
        sn = a1 * n
    return sn

# sprawdza czy kolejne trzy wyrazy tworzą ciąg geometryczny

def czyg(x, y, z):
    if (y ** 2 != x * z):
        return False
    else:
        return True
