"""
ubezpieczony ma dane ... itp ...
mamy ubezpieczonych ...
co możemy z ubezpieczonym zrobić ...
"""
from datetime import date

class Ubezpieczony:
    def __init__(self, name: str, birthdate: str, address: str):
        self.name = name
        self.birthdate = birthdate
        self.age = date.today().year - int(birthdate[:4])
        self.address = address
        self.__pesel = None
        self.__lata_bezszkodowosci = 0
        print(f"Utworzyliśmy obiekt o ID: {id(self)}")

    @property
    def lata_bezszkodowosci(self):
        return self.__lata_bezszkodowosci

    @lata_bezszkodowosci.setter
    def lata_bezszkodowosci(self, ile_lat: int):
        self.__lata_bezszkodowosci = ile_lat

    def dodaj_lata_bezszkodowosci(self, ile_lat: int):
        self.__lata_bezszkodowosci += ile_lat

    def zwroc_wartosc_pesel(self):
        """
        jeśli pesel is None to wyświetl info o konieczności uruchom.
        metody wprow. pesel
        jeśli pesel jest to zwróc
        """
        return self.__pesel

    def wprowadz_pesel(self, wartosc: str):
        """zwaliduj pesel - API: https://h88.pl/sm/api/v1/pesel/verify/?pesel=87300369749
        i wprowadź gdy poprawny, a gdy nie:
        raise Exception("BAD PESEL")
        """
        self.__pesel = wartosc

    def info(self):
        print(f"Ubezpieczony: {self.name}, urodzony w {self.birthdate}, ma lat:{self.age}")
        print(f"PESEL: {self.__pesel}")


ubezpieczony_1 = Ubezpieczony("Adam Jurkiewicz", "1974-03-11", "Warszawa")
ubezpieczony_2 = Ubezpieczony("Beata Jurkiewicz", "1970-05-25", "Warszawa")

print(id(ubezpieczony_1))
print(id(ubezpieczony_2))
print(ubezpieczony_1.name)
print(ubezpieczony_2.name)
ubezpieczony_1.info()
ubezpieczony_2.info()
print(ubezpieczony_2.lata_bezszkodowosci)
# print(ubezpieczony_2.__lata_bezszkodowosci)
ubezpieczony_2.lata_bezszkodowosci = 20
print(ubezpieczony_2.lata_bezszkodowosci)
ubezpieczony_2.dodaj_lata_bezszkodowosci(3)
print(ubezpieczony_2.lata_bezszkodowosci)
ubezpieczony_1.wprowadz_pesel("74031105833")
ubezpieczony_1.info()

