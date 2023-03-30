with open("jatekosok.txt", "r", encoding="utf-8") as fajl:
    jatekosok=[a.strip().split(":") for a in fajl]

def jatekosok_szama():
    for jatekos in jatekosok:
        jatekosok_szama = jatekosok_szama 
print(f"A játékosok száma:{jatekosok_szama} db")
