import requests

start = "2023-12-01"
finish = "2023-12-18"
currency = "CHF"
api_link = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start}/{finish}?format=JSON"

r = requests.get(api_link)
# print("Koniec")
# print(r)
# print(r.content)

json_data = r.json()
print(json_data)

