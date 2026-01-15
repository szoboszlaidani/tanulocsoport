#írj 2 függvényt, a egyik generáljon egy random listát, a másik rendezze sorba, és vegye ki a negatív számokat




#MEGOLDÁS
import random
def gen(min:int,max:int,hossz:int) -> list:
    lista = []#ez a hajó, erre kell felpakolni a ....
    for _ in range(hossz):#annyiszor választunk ...t, ahányszor a főnik kérték
        RANDOM=random.randint(min,max) #választunk egy ...t
        lista.append(RANDOM)# felrakjuk a hajóra
    return lista# a hajót visszaküldjük amerikába



def sort(lista:list) -> list:
    lista.sort()#itt csökkenő sorrendbe rakjuk a ....
    
    #simple
    returnlist=[]#ez a cella, ide rakjuk a nem 0-nál kisebb ....
    for x in lista:#az összes fekát átnézzük
        if x>0:#ha a feka nem kevesebb mint 0, akkor bekerülhet a cellába
            returnlist.append(x)#itt rakjuk be a cellába a nem 0-nál kisebb ....

    #advanced
    returnlist=[x for x in lista if x>0]#itt megöljük az összes minuszos fekát, mert azok 0-nál kisebbek
        #az x-et vesszük, amit a listábol veszünk, de csak akkor ha az x az nagyobb mint nulla
    return returnlist#visszaküldjük a nem 0-nál kisebb ....
    
lista=gen(-10,10,100)
rendezettlista=sort(lista)
print(rendezettlista)