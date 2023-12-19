# init, dziedziczenie, super()

class Pracownik:

    def __init__(self, name, surname, year, place):
        self.imie_nazwisko = name + surname
        self.year = year
        self.place = place
        self.gender = "M" if
        print("Init dla obiektu")


pracownik1 = Pracownik("Adam", "Jurkiewicz", 1999, "Administrator")
print("After")
pracownik1.x = 30

print(dir(pracownik1))