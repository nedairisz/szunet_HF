
# Kérj be egy [200, 920] intervallumban lévő egész számot
# (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!
def feladat1():
    a:int = int(input("Adj meg egy egesz szamot!"))
    while not(a>=200 and a<=920):
        print("A szam 200 es 920 koze kell essen! Probald ujra! ")
        a: int = int(input("Adj meg egy egesz szamot!"))
    print("OK!")


# Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak;
# jelezz hibát, ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”).
# Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”
def feladat4():
    a:int = int(input("Add meg hányadik órában jársz!: "))
    if a == 1:
        print("Még 90%-on vagyunk!")
    elif a==2 or a==3:
        print("Még bírjuk (60%).")
    elif a>=4 and a<=7:
        print("Progit tanulunk, töltődünk! 70%")
    elif a==8 or a==9:
        print("Lassan nem bírjuk tovább! 50%")
    elif a>9:
        print("Ez már tényleg túlzás.")
    elif a==0:
        print("Be se jövök!")
    else:
        print("Hibás óra, adj meg egy érvényes órát 1 és 9 között.")


# Írj metódsut, melynek  2 bemenő prarmétere van (nap neve, óra neve) és tájékoztatást ad Márti állapotáról.
def feladat5():
    nap:str = str(input("Add meg a napot!: "))
    ora:str = str(input("Add meg az orat!: "))
    if nap == "hétfő":
            print("alszik")
    elif nap == "kedd":
        if ora == "hittan":
            print("figyel")
        else:
            print("alszik")
    elif nap == "szerda":
        if ora == "programozás":
            print("dolgozik")
        else:
            print("nincs info")
    elif nap == "csütörtök":
        print("figyel")
    elif nap == "péntek":
        print("félig van jelen")
    else:
        print("nincs info")


# A program számítsa ki egy beolvasott valós szám négyzetgyökét!
# A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
def feladat6():
    a:float = float(input("Adj meg egy pozitiv valos szamot!: "))
    if a>0:
        gyok = a ** 0.5
        print(f"{a:.0f} gyoke: {gyok:.2f}")
    else:
        print("Hiba: Negatív számból nem lehet gyököt vonni!")


# A program olvasson be a konzolról két valós számot!
# Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai.
# A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra!
# Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!
def feladat7():
    a:int = int(input("Adj meg egy valós szaáot!:"))
    b:int = int(input("Adj meg még egy valós számot!:"))
    if a>0 and b>0:
        kerulet = 2*(a+b)
        terulet = a*b
        print(f"A megadott téglalap területe: {terulet:.2f}, kerulete pedig: {kerulet:.2f}")
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")


#A  felhasználónak be kell gépelnie melyik szektort szeretné megnézni,
# a te programod pedig kiírja az ott található kiállítás nevét.
def feladat8():
    szektor:str = str(input("Adja meg a kívánt szektor betűjét (A-H-ig)!:" ))
    if type(szektor) == str and len(szektor) == 1:
        if szektor == "A":
            print("Nemzetközi Csarnok, World Conservation Forum 2021")
        elif szektor=="B" or szektor=="E":
            print("Kereskedelmi Csarnok")
        elif szektor == "C":
            print("Konferencia-központ Innovációs Showroom")
        elif szektor == "D":
            print("Hal, Víz és Ember")
        elif szektor == "F":
            print("Hagyományos Vadászati Módok Csarnoka")
        elif szektor == "G":
            print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
        elif szektor == "H":
            print("Központi Magyar Kiállítás")
        else:
            print("Forduljon a pénztárhoz'")
    else:
        print("HIBA: Adjon meg egy betűt A-H-ig!")

# Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!
def feladat9():
    i = 1
    while i<=10:
        eredmeny = i*10
        print(f"{i} * 10 = {eredmeny}", end="\n")
        i+=1

# Írj metódust, mely neveket kér a felhasználótól addig amíg a „@” jelet nem kapja.
# Hány nevet adott meg a felhasználó?
# Van-e benne A betűvel kezdődő név?
# Melyik a leghosszabb név?
def feladat10():
    nev:str = str(input("Adj meg egy nevet!:" ))
    while not(nev=="@"):
        nev: str = str(input("Adj meg egy nevet!:"))
    print("Kész.")

# Írj metódust, mely egy érmedobás eredményét kéri be a felhasználótól 10-szer egymás után!
# A felhasználó minden lépésben a „f” vagy  „i” betűket kell megadjon. Addig kérd be a jeleket, amíg jó jelet nem ad meg.
# Hányszor adott meg „f” betűt?
# Mekkora a leghosszabb f sorozat?
def feladat11():
    eredmenyek = ""
    i = 0
    while i < 10:
        eredmeny = input("Fej vagy irás? (f/i): ")
        if eredmeny == "f" or eredmeny == "i":
            eredmenyek += eredmeny
            i += 1
        else:
            print("Érvénytelen eredmény! Csak 'f' vagy 'i' elfogadott.")
    print(f"{eredmenyek}")
    print(f"{eredmenyek.count('f')} alkalommal fordult elő 'f'.")

"""
    maxhossz = 0
    hossz = 0
    for eredmeny in eredmenyek:
        if eredmeny == "f":
            hossz += 1
            if hossz > maxhossz:
                maxhossz = hossz
        else:
            hossz = 0
    print(f"A leghosszabb f sorozat hossza: {maxhossz}")
"""

def feladat11_2():
    i:int = 0
    f_szama:int=0
    fhossz:int=0
    elozo_string_f=False
    max_hossz=0
    while i<10:
        jel:str = input("F/I: ")
        while not((jel=="F") or (jel=="f") or (jel=="I") or (jel=="i")):
            jel:str = input("nem jó, F/I adj meg!")
        if(jel=="F" or jel=="f"):
            f_szama+=1
            if elozo_string_f:
                fhossz+=1
            elozo_string_f=True
        else:
            print("Aktuális hossz ",fhossz)
            elozo_string_f=False
            #itt összehasonlítjuk az eddigi maxhosszt az aktuális hosszal
            if(max_hossz<fhossz):
                max_hossz=fhossz
            fhossz=0
        i+=1
    print("aktuális hossz: ", fhossz)
    if(max_hossz<fhossz):
                max_hossz=fhossz
    print("F-ek száma: ", f_szama)
    print("maximális F hossz: ", max_hossz)
    



# 2. feladat. Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! 
# használd hozzá az egész osztás operátorát - // ! pl: 123//10 =12  123%10=3
def szam_szamjegye(szam:int):
    print("szám: ", szam)
    while(szam>9):
        print("következő számjegy", szam%10)
        szam= szam//10
        print("az aktuális szám ", szam)
    print("Az utolsó számjegy ", szam)

def szam_szamjegye2(szam:int):
    szoveg_szam:str=str(szam)
    i=0
    while i<=len(szoveg_szam):
        print(szoveg_szam[i])
        i+=1

