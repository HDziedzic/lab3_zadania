import random
import sys
from ciągi import arytmetyczny, geometryczny
# zadanie 1


print("-----------------zad_1----------------------")
a = [1 - x for x in range(1, 10)]
b = [pow(4, n) for n in range(7)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)

# zadanie 2
print("-----------------zad_2----------------------")
# sposób z pentlą
# for i in range(10):
#     lista1.append(random.randint(1, 200))

# Python Comprehension:
lista1 = [random.randint(1, 200) for i in range(10)]
parzyste = [x for x in lista1 if x % 2 == 0]

print(parzyste)

# zadanie 3
print("-----------------zad_3----------------------")

slownik = {"kawa": "kg",
           "Mąka": "kg",
           "Chleb": "szt.",
           "herbata": "szt.",
           "cukier": "kg"}
szt = {k: v for (k, v) in slownik.items() if v == "szt."}
print(szt)

# zadanie 4

print("-----------------zad_4----------------------")
# za pomocą if`ów
# def czy_pr(A, B, C):
#     if A > B and A > C:
#         if B ** 2 + C**2 == A ** 2:
#             print("jest prostokątny")
#         else:
#             print("nie jest prostokątny")
#     if B > A and B > C:
#         if A ** 2 + C**2 == B ** 2:
#             print("jest prostokątny")
#         else:
#             print("nie jest prostokątny")
#     if C > B and C > A:
#         if B ** 2 + A**2 == C ** 2:
#             print("jest prostokątny")
#         else:
#             print("nie jest prostokątny")
#
# czy_pr(5, 4, 3)
# czy_pr(5, 3, 4)
# czy_pr(5, 3, 3)
def czy_pr2(A, B, C):
    boki = [A, B, C]
    m = boki.index(max(A, B, C))
    x = boki.pop(m) ** 2
    if x == boki[0] ** 2 + boki[1] ** 2:
        print("jest prosotkątny")
    else:
        print("nie jest prosotkątny")


czy_pr2(6, 10, 8)
czy_pr2(5, 13, 12)
czy_pr2(5, 3, 3)
# zadanie 5
print("-----------------zad_5----------------------")


def pole_trapezu(a, b, h):
    pole = ((a + b) * h) / 2
    return pole


print("pole trapezu wynosi:")
print(pole_trapezu(6, 4, 5))
# zadanie 6
print("-----------------zad_6----------------------")


def iloczyn_wyr_ciagu(a, b, ile):
    for i in range(ile):
        a *= b
    return a


print(iloczyn_wyr_ciagu(1, 4, 10))

# zadanie 7
print("-----------------zad_7----------------------")


def zad_7_iloczyn_wyr_ciagu(b, *a):
    if len(a) == 0:
        return 0
    else:
        iloczyn = 0
        wynik = 0
        for i in range(len(a)):
            iloczyn = a[i] * b
            wynik += iloczyn

        return wynik


print(zad_7_iloczyn_wyr_ciagu(2, 3, 6, 12))

# zadanie 8
print("-----------------zad_8----------------------")


def l_zakupy(**zakupy):
    for produkt in zakupy:
        print(produkt, ":")
        print(zakupy[produkt], "zł")
    ile = len(zakupy)
    print("liczba produktów: ", ile)
    print("Razem do zapłaty: {liczba:.2f} zł".format(liczba=sum(zakupy.values())))


l_zakupy(czekolada=4.99, chleb=2, masło=6.89, woda=4.21)

# zadanie 9
print("-----------------zad_9----------------------")

print(arytmetyczny.wyr_n(1, 4, 2))
print(geometryczny.sum(4, 1, 2))

# zadanie 10
print("-----------------zad_10----------------------")

f = [x for x in range(0, 100) if x % 4 == 0]
plik = open("zad_10.txt", "w+")
plik.writelines(str(f))
plik.close()

# zadanie 10
print("-----------------zad_10----------------------")
plik = open("zad_10.txt", "r")
wiersze = plik.readlines()
plik.close()
print(wiersze)
