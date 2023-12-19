"""
ubezpieczony ma dane ... itp ...
mamy ubezpieczonych ...
co możemy z ubezpieczonym zrobić ... dodaj metody wprowadzania pesel
"""
from datetime import date

class Ubezpieczony:
    def __init__(self, name: str, birthdate: str, address: str):
        self.name = name
        self.birthdate = birthdate
        self.age = date.today().year - int(birthdate[:4])
        self.address = address
        self.pesel = None
        self.__lata_bezszkodowosci = 0
        print(f"Utworzyliśmy obiekt o ID: {id(self)}")

    def info(self):
        print(f"Ubezpieczony: {self.name}, urodzony w {self.birthdate}, ma lat:{self.age}")


ubezpieczony_1 = Ubezpieczony("Adam Jurkiewicz", "1974-03-11", "Warszawa")
ubezpieczony_2 = Ubezpieczony("Beata Jurkiewicz", "1970-05-25", "Warszawa")

print(id(ubezpieczony_1))
print(id(ubezpieczony_2))
print(ubezpieczony_1.name)
print(ubezpieczony_2.name)
ubezpieczony_1.info()
ubezpieczony_2.info()

# print(ubezpieczony_2.__lata_bezszkodowosci) - tu będzie błąd
