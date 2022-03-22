# n-ty wyraz ciagu
def wyr_n(a1, r, n):
    a_n = a1 + (n - 1) * r
    return a_n

wyr_n(1, 4, 10)

# n-ty wyraz ciagu ze wzoru na sumę
def wyr_ns(a1, n, r):
    an = ((2 * a1 + (n - 1) * r) / 2) * n - (((2 * a1 + (n - 1) * r) / 2) * n) - 1
    return an

# wzory na sumę ciagu

def sum(a1, an, n):
    sn = ((a1 + an) / 2) * n
    return sn
def sumv(a1, r, n):
    sn = ((2 * a1 + (n - 1) * r) / 2) * n
    return sn