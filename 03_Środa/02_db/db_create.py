from tinydb import TinyDB, Query, where
from random import choice
from faker import Faker

db = TinyDB('db_users_cities.json')
# na wszelki wypadek czyścimy
db.drop_tables()

table_users = db.table("tabela_users")
table_city = db.table("tabela_miasto")

dane = Faker(["pl_PL"])

for _ in range(30):
    miasto_losowe = choice(("Warszawa", "Poznań", "Gdańsk", "Wrocław"))
    ID_user = dane.pesel()
    table_users.insert({"ID": ID_user, "Imie": dane.name().split()[-2], "Nazwisko": dane.name().split()[-1]})
    table_city.insert({"ID": ID_user, "Miasto": miasto_losowe})