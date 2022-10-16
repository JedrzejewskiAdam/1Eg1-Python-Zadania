print("z1")
su = int(input("Podaj liczbę pierwszą : "))
ma = int(input("Podaj liczbę drugą : "))
if (su + ma) % 2 == 0:
    print("parzysta")
else:
    print("nieparzysta")

print("z2")
sredniapierwsza = float(input("Podaj pierwszą średnią : "))
sredniadruga = float(input("Podaj drugą średnią : "))
from math import sqrt
if (sredniapierwsza + sredniadruga) / 2 > sqrt(sredniapierwsza * sredniadruga) :
    print("tak średnia arytmetyczna jest większa")
else :
    print("nie średnia geometryczna jest większa")

print("z3")
liczbapierwsza = int(input("Podaj pierwszą liczbę : "))
liczbadruga = int(input("Podaj drugą liczbę : "))
liczbatrzecia = int(input("Podaj trzecią liczbę: "))
if liczbapierwsza == liczbatrzecia or liczbapierwsza == liczbadruga or liczbadruga == liczbatrzecia : 
    print("przynajmniej 2")
    if liczbapierwsza == liczbadruga and liczbapierwsza == liczbatrzecia and liczbadruga == liczbatrzecia :
        print("wszystkie")
    elif liczbapierwsza == liczbadruga :
        print("pierwsza i druga")
    elif liczbadruga == liczbatrzecia :
        print("druga  i trzcia")
    elif liczbapierwsza == liczbatrzecia :
        print("pierwsza i trzecia")
else :
    print("nie")

print("z4")
pierwszaliczba = int(input("Podaj pierwszą liczbę : "))
drugaliczba = int(input("Podaj drugą liczbę : "))
trzecialiczba = int(input("Podaj trzecią liczbę : "))
czwartaliczba = int(input("Podaj czwartą liczbę : "))
if czwartaliczba < pierwszaliczba and czwartaliczba < drugaliczba and czwartaliczba < trzecialiczba :
    print("najmniejsza to ",czwartaliczba)
elif trzecialiczba < pierwszaliczba and trzecialiczba < drugaliczba and trzecialiczba < czwartaliczba :
    print("najmniejsza to ",trzecialiczba)
elif pierwszaliczba < drugaliczba and pierwszaliczba < trzecialiczba and pierwszaliczba < czwartaliczba:
    print("najmniejsza to ",pierwszaliczba)
elif drugaliczba < pierwszaliczba and drugaliczba < trzecialiczba and drugaliczba < czwartaliczba :
    print("najmniejsza to ",drugaliczba)
else :
    print("Coś poszło nie tak :(")

print("z5")
pierwszyboktrojkata = int(input("Podaj pierwszy bok trójkąta : "))
drugiboktrojkata = int(input("Podaj drugi bok trójkąta : "))
trzeciboktrojkata = int(input("Podaj trzeci bok trójkąta : "))
if drugiboktrojkata - trzeciboktrojkata < pierwszyboktrojkata < drugiboktrojkata + trzeciboktrojkata and pierwszyboktrojkata - trzeciboktrojkata < drugiboktrojkata < pierwszyboktrojkata + trzeciboktrojkata and pierwszyboktrojkata - drugiboktrojkata < trzeciboktrojkata < pierwszyboktrojkata + drugiboktrojkata :
    print("spełnia")
else :
    print("nie spełnia")

print("z6")
pierwszybok = int(input("Podaj pierwszy bok trójkąta : "))
drugibok = int(input("Podaj drugi bok trójkąta : "))
trzecibok = int(input("Podaj trzeci bok trójkąta : "))
if pierwszybok < drugibok + trzecibok and drugibok < pierwszybok + trzecibok and trzecibok < pierwszybok + drugibok : 
    print("może powstać")
    if pierwszybok**2 + drugibok**2 < trzecibok**2 or drugibok**2 + trzecibok**2 < pierwszybok**2 or trzecibok**2 + pierwszybok**2 < drugibok**2 :
        print("rozwartokątny")
    elif pierwszybok**2 + drugibok**2 == trzecibok**2 or drugibok**2 + trzecibok**2 == pierwszybok**2 or trzecibok**2 + pierwszybok**2 == drugibok**2 : 
        print("prostokątny")
    elif pierwszybok**2 + drugibok**2 > trzecibok**2 or drugibok**2 + trzecibok**2 > pierwszybok**2 or trzecibok**2 + pierwszybok**2 > drugibok**2 :
        print("ostrokątny")
else :
    print("Nie ma szans")