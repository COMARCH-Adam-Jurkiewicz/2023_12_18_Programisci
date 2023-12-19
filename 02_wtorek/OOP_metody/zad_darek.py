class Prostokat:
    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        return 2*(self.a + self.b)

    def pole(self):
        return self.a * self.b

class Kwadrat(Prostokat):
    def __init__(self, a):
        super(). __init__(a, a)

prostokat = Prostokat(4, 6)
kwadrat= Kwadrat(5)

print(f"Prostokąt - obwód:", prostokat.obwod())
print(f"Prostokąt - pole:", prostokat.pole())

print(f"Kwadrat - obwod:", kwadrat.obwod())
print(f"Kwadrat - pole:", kwadrat.pole())