def atlag(lista:list)->float:#1
    osszeg=0
    for szam in lista:
        osszeg+=szam
    return osszeg/len(lista)

def paros_db(lista:list)->int:#2
    db=0
    for szam in lista:
        if szam%2==0:
            db+=1
    return db

def legkisebb(lista:list)->int:#3
    min_elem=lista[0]
    for szam in lista:
        if szam<min_elem:
            min_elem=szam
    return min_elem

def nagyobb_5(lista:list)->int:#4
    db=0
    for szam in lista:
        if szam>5:
            db+=1
    return db

def szoroz3(lista:list)->list:#5
    uj=[]
    for szam in lista:
        uj.append(szam*3)
    return uj

def egyjegyuek(lista:list)->list:#6
    uj=[]
    for szam in lista:
        if -9<=szam<=9:
            uj.append(szam)
    return uj

def oszthato3(lista:list)->int:#7
    db=0
    for szam in lista:
        if szam%3==0:
            db+=1
    return db

def listabol_szam(lista:list)->int:#8
    szam=0
    for i in lista:
        szam=szam*10+i
    return szam

def csere(lista:list)->list:#9
    temp=lista[0]
    lista[0]=lista[-1]
    lista[-1]=temp
    return lista

def novekvo(lista:list)->bool:#10 - NEHÉZ
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True