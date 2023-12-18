def parsuj(*args):
    pass


lista_przedzialow = []

with open("przedzialy.txt", "r") as dane:
    lines = dane.readlines()

for i in lines:
    przecinek = i.index(",")
    if i[0] == "<":
        pierwsza_liczba = int(i[1:przecinek])
    else:
        pierwsza_liczba = int(i[1:przecinek]) + 1

    liczba_znakow = len(i)

    if i[liczba_znakow - 1] == ">":
        druga_liczba = int(i[przecinek + 1:liczba_znakow - 2])
    else:
        druga_liczba = int(i[przecinek + 1:liczba_znakow - 2]) - 1

    lista_robocza = []
    x = range(pierwsza_liczba, druga_liczba + 2, 1)
    for n in x:
        lista_robocza.append(n)

    lista_przedzialow.append(lista_robocza)

print(f"Wynik: {lista_przedzialow=}")