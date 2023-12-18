import requests
from nbp_funkcje import *



start = ""
finish = data_inna_koncowa()
ile_dni = oblicz_ilosc_dni(days=9)

start = finish - ile_dni
# print(f"{start=}")

kody_ok = (
    'USD',
    'CHF',
    "EUR",
    "AUD",
)

currency_ok = False
while not currency_ok:
    currency = input("Podaj kod waluty w formacie XXX: ")
    currency = currency.upper()
    currency_ok = currency in kody_ok

api_link = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start}/{finish}?format=JSON"

r = requests.get(api_link)
# print("Koniec")
# print(r)
# print(r.content)

json_data: dict = r.json()
# print(json_data)

kursy_waluty = json_data["rates"]

wart = 0
ile = 0
for element in kursy_waluty:
    # print(f"{element=}")
    wart += element["mid"]
    ile += 1

sredni_kurs = wart / ile
print(f'Średni kurs dla {json_data["currency"]} w okresie {start} do {finish} wynosi {sredni_kurs} zł.')
