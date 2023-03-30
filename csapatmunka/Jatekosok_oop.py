class Focistak:
    def __init__(self,nev,csapat,gol):
        self.nev = nev
        self.csapat = csapat
        self.gol = gol
fajl = open("jatekosok.txt","r",encoding="utf-8")

jatekosok_lista = []
for sorok in fajl:
    oszlop = sorok.strip().split(":")
    jatekosok_lista.append(Focistak(oszlop[0], oszlop[1], oszlop[2]))

for item in jatekosok_lista:
    print(f"Név: {item.nev}, Csapat: {item.csapat}, Gól: {item.gol}")

 

def jatekosok_szama():
    print(f"A focisták száma: {len(jatekosok_lista)} fő")
jatekosok_szama()

def focistak_golossz():
    ossz = 0
    for item in jatekosok_lista:
        ossz = ossz + int(item.gol)
    print(f"A játékosok összgóljaik: {ossz} gól")
focistak_golossz()

legtöbb = max(int(j.gol) for j in jatekosok_lista)
for item in jatekosok_lista:
    if int(item.gol) == legtöbb:
        print(f"A legtöbb gólt lövő: {item.nev}")