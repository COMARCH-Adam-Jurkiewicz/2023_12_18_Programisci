def parsuj(element):
    separator = element.find(",")
    a = element[1:separator]
    b = element[separator + 1:-1]

    if element[0] == '(':
        a = int(a) + 1
    else:
        a = int(a)

    if element[-1] == ')':
        b = int(b) - 1
    else:
        b = int(b)

    wynik = list(range(a, b + 1))

    return wynik


lista_przedzialow = []
with open("przedzialy.txt", "r") as dane:
    zpliku = dane.readlines()
    # print(f"{zpliku=}")

for element in zpliku:
    nowa = parsuj(element.strip())
    lista_przedzialow.append(nowa)

print(f"Wynik: {lista_przedzialow=}")