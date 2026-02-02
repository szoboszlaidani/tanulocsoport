import random
# 1️⃣ Átlag kiszámítása
def atlag(lista):
    if len(lista) == 0:
        return 0
    osszeg = 0
    for szam in lista:
        osszeg += szam
    return osszeg / len(lista)


# 2️⃣ Páros számok számlálása
def poros_szamok(lista):
    szamlalo = 0
    for szam in lista:
        if szam % 2 == 0:
            szamlalo += 1
    return szamlalo


# 3️⃣ Legkisebb elem (min nélkül)
def legkisebb(lista):
    if len(lista) == 0:
        return None
    minimum = lista[0]
    for szam in lista:
        if szam < minimum:
            minimum = szam
    return minimum


# 4️⃣ Nagyobb, mint 5
def nagyobb_mint_5(lista):
    szamlalo = 0
    for szam in lista:
        if szam > 5:
            szamlalo += 1
    return szamlalo


# 5️⃣ Lista szorzása 3-mal
def lista_szorozo_3(lista):
    uj_lista = []
    for szam in lista:
        uj_lista.append(szam * 3)
    return uj_lista


# 6️⃣ Egyjegyű számok megtartása
def csak_egyjegyu(lista):
    uj_lista2 = []
    for szam in lista:
        if -9 <= szam <= 9:
            uj_lista2.append(szam)
    return uj_lista2