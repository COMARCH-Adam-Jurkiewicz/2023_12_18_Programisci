import requests

start = "2023-12-01"
finish = "2023-12-18"
currency = "CHF"
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
    print(f"{element=}")
    wart += element["mid"]
    ile += 1

sredni_kurs = wart / ile
print(f'Średni kurs dla {json_data["currency"]} w okresie {start} do {finish} wynosi {sredni_kurs} zł.')
