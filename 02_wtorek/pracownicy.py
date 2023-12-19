"""
Utworz klasę Pracownik z właściwościami:
- id - id_obiektu jako str
- imie
- nazwisko
- pesel, walidowany za pomocą API: https://h88.pl/sm/api/v1/pesel/verify/?pesel=87300369749
- płeć (ustawiane bazując na ostatniej literze imienia lub jesli podano jako parametr)
- numer telefonu, opcjonalne dane z https://apilayer.com/marketplace/number_verification-api)
- kod i opis działu (4 różne działy wymyślić)
- wynagrodzenie brutto / miesiąc
- ilość godzin do przepracowania miesięcznie, domyślnie 160
- realna ilośc godzin wypracowana w miesiącu
- wynagr. netto za godz, obl. brutto - 40%
- słownik godzin nadliczbowych w miesiącach
==========
Metody:
- info
- wprowadz. ilości godzin w miesiącu (min. 160, max. 200)
- obliczenie wynagrodzenia podstawowego
- oblicznie wynagrodzenia dodatkowego + zapis do pola w słowniku
- wypisanie podatków pobranych od początku roku
- wypisanie kwoty netto do wypłaty za ostatni miesiąc
- info o dotychczasowych wypłatach w kolejnych miesiącach
"""