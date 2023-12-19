import csv
from faker import Faker

# https://faker.readthedocs.io/en/master/locales.html
locales = ("pl_PL", "it_IT", "jp_JP", "ru_RU", "sl_SI", "sv_SE", "tw_GH", "de_DE")
dane_all = []

header= ["nazwa", "firma", "telefon", "pesel"]
for lang in locales:
    dane = Faker(lang)
    print(f"-------[ {lang=} ]--------")
    for _ in range(20):
        pesel = dane.pesel() if lang == "pl_PL" else "xxx"
        poz = [dane.name(), dane.company(), dane.phone_number(), pesel]
        dane_all.append(poz.copy())


# zamień kod tak, by generował po 20 przykładów dla 1 locale

with open('dane.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(dane_all)