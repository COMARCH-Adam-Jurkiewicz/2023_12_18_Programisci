import requests
from datetime import date, timedelta

start = ""
data_ok = False
while not data_ok:
    try:
        finish = input("Podaj datę końcową w formacie RRRR-MM-DD: ")
        finish = date.fromisoformat(finish)
        data_ok = True
    except:
        finish = date.fromisoformat('2023-12-01')
    finally:
        # wykona się zawsze niezależnie od ty/except
        print("xxxxxxxxxxx")

ile_dni = int(input("Ile dni wstecz (max. 14): "))
ile_dni = timedelta(days=ile_dni if ile_dni <= 14 else 14)

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
