def znajdz_liczby_w_tekscie(text):
    liczby = []
    tmp = ''
    for char in text:
        if char == '-' or char.isnumeric():
            tmp += char
        if char == ',':
            liczby.append(int(tmp))
            tmp = ''
        else:
            pass

    liczby.append(int(tmp))
    return liczby


def parsuj(text):
    liczby = znajdz_liczby_w_tekscie(text)

    if text[0] == '(':
        liczby[0] += 1
    if text[-1] == ')':
        liczby[1] -= 1

    print(liczby)

    return range(liczby[0], liczby[1])


lista_przedzialow = []

with open("przedzialy.txt", "r") as dane:
    z_pliku = dane.readlines()

for row in z_pliku:
    lista_przedzialow.append(parsuj(row.strip()))

print(f"Wynik: {lista_przedzialow=}")