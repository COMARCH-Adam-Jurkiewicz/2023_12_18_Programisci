# init, dziedziczenie, super()

class Pracownik:

    def __init__(self, name, surname, year, place):
        self.imie_nazwisko = name + surname
        self.year = year
        self.place = place
        self.gender = "M" if name[-1] != "a" else "F"
        print("Init dla obiektu")

    def show(self):
        print(f"Pracownik {self.imie_nazwisko}, zatrudniony na stanowisku {self.place} od roku {self.year}.")


pracownik1 = Pracownik("Adam", "Jurkiewicz", 1999, "Administrator")
print("After")
pracownik1.x = 30

print(dir(pracownik1))