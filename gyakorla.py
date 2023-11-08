import random
import math
# véletlen számok generálása
def veletlen():
    #[10,30] közötti véletlen számokat
    i:int =0
    while i<10:
        szam:int = math.floor(random.random()*21+10)
        print(szam, end=" ")
        i+=1

# 1. Generálj 5 véletlen lottószámot [1,90]
def gyak1():
    i:int =0
    while i<5:
        szam:int = math.floor(random.random()*81+10)
        print(szam, end=" ")
        i+=1

# 2. Generálj 1 kétjegyű véletlen számot. Döntsd el róla h páros vagy páratlan
def gyak2():
    i:int =0
    while i<1:
        szam:int = math.floor(random.random()*90+10)
        print(szam, end=" ")
        if szam%2==0:
            print(f"{szam} páros!")
        else:
            print(f"{szam} páratlan!")
        i+=1

# 3. Generálj 15 egész számot [0,1] között. Hány 1-est generáltál?
def gyak3():
    i:int =0
    while i<15:
        szam:int = math.floor(random.random()*2)
        print(szam, end=" ")
        i+=1

# 4. Generálj egy véletlen számot 1 és 10 között! Szorozd meg 3-al, vonj ki belőle 15-öt, osztd el 6-al, szorozd be 2-vel. 
# Vond ki belőle az edeti számot. A program írja ki. h ez eredmény egyenlő-e 5-tel?
def gyak4():
    i:int =0
    while i<1:
        szam:int = math.floor(random.random()*)
        print(szam, end=" ")
        i+=1



# 5. Írj metódust, mely a paraméterében kapott szövegnek kiírja a hosszát. Az 5. karakterét nagybetűvel.