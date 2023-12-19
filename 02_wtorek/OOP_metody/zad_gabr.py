class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        print(f"Obwód wynosi {(2*self.a)+(2*self.b)}j")

    def pole(self):
        print(f"Obwód wynosi {self.a*self.b}j^2")

class Kwadrat(Prostokat):

    def __init__(self, a):
        super().__init__(a, a)

