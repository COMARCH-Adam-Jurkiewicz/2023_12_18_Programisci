import requests
from datetime import date, timedelta
def oblicz_ilosc_dni(days=7):
    try:
        ile_dni = int(days)
        if ile_dni < 0:
            ile_dni *= -1
    except:
        ile_dni = 7
    return timedelta(days=ile_dni if ile_dni <= 14 else 14)

def get_values(code: str, last_date: str, days: str) -> list:
    """

    :param code: "CHF lub USD"
    :param last_date: data w formacie RRRR-MM-DD
    :param days: liczba dni
    :return: lista wartości waluty, np.: [4.234, 4.214]
    """
    last_date = date.fromisoformat(last_date)
    start_date = last_date - oblicz_ilosc_dni(days)
    api_link = f"https://api.nbp.pl/api/exchangerates/rates/A/{code}/{start_date}/{last_date}?format=JSON"
    r = requests.get(api_link)
    json_data: dict = r.json()
    kursy_waluty = json_data["rates"]
    wart = []
    for element in kursy_waluty:
        wart.append(element["mid"])

    print(f" From {api_link} got {wart}.")
    return wart