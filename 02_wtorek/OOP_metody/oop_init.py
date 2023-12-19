# init, dziedziczenie, super()

class Pracownik:

    def __init__(self, name, surname, year, place):
        self.imie_nazwisko = f"{name} {surname}"
        self.year = year
        self.place = place
        self.gender = "M" if name[-1] != "a" else "F"
        print(f"Init dla obiektu: {id(self)}")

    def show(self):
        print(f"Pracownik {self.imie_nazwisko}, zatrudniony na stanowisku {self.place} od roku {self.year}.")

    def set_salary(self, new_salary_net: int):
        # dodaj nową pensję miesięczną netto i brutto + 40%
        self.new_salary_net = new_salary_net

    def show_salary(self):
        # wypisz info o pensji netto i brutto
        print(f"Pracownik {self.imie_nazwisko}, zatrudniony na stanowisku {self.place} od roku {self.year} zarabia aktualnie {self.new_salary_net} zł netto, co stanowi {self.new_salary_net*1.4} zł brutto.")


pracownik1 = Pracownik("Adam", "Jurkiewicz", 1999, "Administrator")
pracownik2 = Pracownik("Beata", "Jurkiewicz", 1995, "Handlowiec")
print("After")
print(id(pracownik1))
print(id(pracownik2))

pracownik1.show()
pracownik2.show()

