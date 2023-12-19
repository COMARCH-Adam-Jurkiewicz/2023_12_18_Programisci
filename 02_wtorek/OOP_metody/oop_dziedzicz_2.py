#  super()
#

class Pracownik:

    def __init__(self, name, surname, year, place):
        self.imie_nazwisko = f"{name} {surname}"
        self.year = year
        self.place = place
        self.gender = "M" if name[-1] != "a" else "F"
        self.new_salary_net = 100
        self.salary_gross = 160
        print(f"Init dla obiektu: {id(self)}")

    def show(self):
        print(f"Pracownik {self.imie_nazwisko}, zatrudniony na stanowisku {self.place} od roku {self.year}.")

    def set_salary(self, new_salary_net: int):
        # dodaj nową pensję miesięczną netto i brutto + 40%
        self.new_salary_net = new_salary_net
        self.salary_gross = self.new_salary_net * 1.4

    def show_salary(self):
        # wypisz info o pensji netto i brutto
        print(f"Pracownik {self.imie_nazwisko}, zatrudniony na stanowisku {self.place} od roku {self.year} zarabia aktualnie {self.new_salary_net} zł netto, co stanowi {self.salary_gross} zł brutto.")


class Zarzad(Pracownik):

    def __init__(self, name, surname, year):
        super().__init__(name, surname, year, "Zarząd spólki")
        print(f"Super wykonano -> slary: {self.salary_gross}")


    def show(self):
        print(f"Cłonek zarządu: {self.imie_nazwisko} od roku {self.year}")

    def show_place(self):
        print(f"Miejsce pracy: {self.place}")


pracownik1 = Pracownik("Adam", "Jurkiewicz", 1999, "Administrator")
pracownik2 = Pracownik("Beata", "Jurkiewicz", 1995, "Handlowiec")

czlonek1 = Zarzad("Adam", "Jurkiewicz", 2020)

print("After")
print(id(pracownik1))
print(id(pracownik2))

pracownik1.show()
pracownik2.show()

czlonek1.show()
czlonek1.show_place()

pracownik1.show_salary()

czlonek1.show_salary()