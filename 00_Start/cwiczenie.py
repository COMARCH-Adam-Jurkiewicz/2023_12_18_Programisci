def parsuj(element):
    return element


lista_przedzialow = []


with open("przedzialy.txt", "r") as dane:
    zpliku = dane.readlines()
    # print(f"{zpliku=}")

for element in zpliku:
    nowa = parsuj(element.strip())
    print(f"{nowa=}")


print(f"Wynik: {lista_przedzialow=}")
