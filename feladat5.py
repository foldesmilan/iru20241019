import math

def ot():
    szam = int(input("Kérem adjon meg egy 40 és 95 között számot!"))
    if szam <40 or szam > 95:
        print("HIBA: nem megfelelő szám")
    else:
        # megoldás
        szam = str(szam)
        print(szam[0])

        # megoldás 2:
        szam = int(szam)
        print(str(int(szam/10)))

        # megoldás 3:
        szam = int(szam)
        print(math.floor((szam/10)))
