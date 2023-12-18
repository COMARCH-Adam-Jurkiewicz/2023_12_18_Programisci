from datetime import date, timedelta

print("test importu.")

def data_koncowa1():
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

    return finish

def data_inna_koncowa():
    while True:
        try:
            finish = input("Podaj datę końcową w formacie RRRR-MM-DD: ")
            finish = date.fromisoformat(finish) if finish else date.today()
            print(f"{finish=}")
            return finish
        except:
            print("Podaj poprawną datę.")

def oblicz_ilosc_dni(days=7):
    try:
        ile_dni = int(input("Ile dni wstecz (max. 14): "))
    except:
        ile_dni = days
    return timedelta(days=ile_dni if ile_dni <= 14 else 14)

