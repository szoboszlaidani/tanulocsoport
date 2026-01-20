#Írj egy függvényt, ami létrehoz egy adott hosszúságú listát véletlen számokkal, majd egy másik függvényt, ami megszámolja, hány páros szám van benne.

#SEGÍTSÉG
import random

def létrehoz(hossz:int,alsó:int,felső:int)->list:#generál függvény, ezt már elvileg tudjátok
    lista = []
    for i in range(hossz):
        szám=random.randint(alsó,felső)
        lista.append(szám)
    return lista

x=2
print(x%2==0)#így nézzük meg hogy egy szám páros-e (maradékos osztás 2-vel, ha a maradékos osztásnak nincs maradéka, akkor a szám osztható 2-vel, tehát páros)

#Írj egy függvényt, ami bekér egy számot, és visszaadja az összes nála kisebb pozitív szám listáját.

#SEGÍTSÉG


#Készíts hatos lottót 

#MEGOLDÁS
def generál(hossz:int,alsó:int,felső:int)->list:#generál függvény, ezt már elvileg tudjátok
    lista = []
    while len(lista)<hossz:
        szám=random.randint(alsó,felső)
        if szám not in lista:
            lista.append(szám)
    return lista


mennyi={}
tipp = generál(6,1,45)
for hét in range(52):
    heti=generál(6,1,45)
    print(heti)
    találat=0
    for tal in range(len(tipp)):
        if tipp[tal]==heti[tal]:
            találat+=1
    if találat in mennyi.keys():
        mennyi[találat]+=1
    else: mennyi[találat]=1

print(mennyi)
#Készíts egy függvényt, ami egy listából kiválogatja a 10-nél nagyobb számokat.


#Írj egy függvényt, ami egy listában megkeresi a legnagyobb számot (ne használd a max()-ot).


#Írj két függvényt:
#   az egyik generál egy random listát
#   a másik megfordítja a lista sorrendjét


#Írj egy függvényt, ami egy listából eltávolítja az összes 0 értéket.


#Készíts egy függvényt, ami megszámolja, hányszor fordul elő egy adott szám egy listában.


#Írj egy függvényt, ami egy listát növekvő sorrendbe rendez (ne használd a sort()-ot).


#Írj egy függvényt, ami egy listából csak a negatív számokat tartja meg.


#Készíts egy függvényt, ami egy listában minden számot megszoroz 2-vel, és egy új listát ad vissza.


#Írj egy függvényt, ami eldönti egy számról, hogy benne van-e egy listában.


#Írj két függvényt:
#   az egyik generál egy random listát
#   a másik kiszámolja a lista elemeinek összegét


#Készíts egy függvényt, ami egy listából eltávolítja az ismétlődő elemeket.


#Írj egy függvényt, ami megszámolja, hány negatív, pozitív és nulla szám van egy listában.


