class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        wynik = 2 * self.a + 2 * self.b
        return (wynik)

    def pole(self):
        wynik = self.a * self.b
        return (wynik)


class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)


a = 3
b = 5
test_prostokat = Prostokat(a, b)
test_kwadrat = Kwadrat(a)
print(f"obwód kwadratu: {test_kwadrat.obwod()}")
print(f"pole kwadratu: {test_kwadrat.pole()}")
print(f"obwód prostokąta: {test_prostokat.obwod()}")
print(f"pole prostokąta: {test_prostokat.pole()}")