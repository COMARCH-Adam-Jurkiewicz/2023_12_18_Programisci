from faker import Faker
# https://faker.readthedocs.io/en/master/locales.html

dane = Faker(["pl_PL", "it_IT", "jp_JP",
              "ru_RU", "sl_SI", "sv_SE" ,
              "tw_GH", "de_DE"])

for _ in range(200):
    print(dane.name(), dane.company(), dane.phone_number(), dane.pesel())

# zamień kod tak, by generował po 20 przykładów dla 1 locale