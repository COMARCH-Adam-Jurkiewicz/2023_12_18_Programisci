class First:
    def __init__(self, parametr1):
        print("INIT 1")
        self.parametr1 = parametr1
    def run(self):
        print(f"running from first - {self.parametr1=}")

class Second:
    def run(self):
        print("running from second")

class Third(First):
    def __init__(self, parametr3, tmp_parametr1):
        super().__init__(tmp_parametr1)  # jakby => obiekt = First(tmp_parametr1)
        self.parametr3 = parametr3
        self.parametr2 = tmp_parametr1

    def third_run(self):
        print(f"running from third - {self.parametr3} - {self.parametr1}")

    def run(self):
        super().run()
        print("Teraz run 3 - cosik")


first = First("Adam 1")
second = Second()
third = Third("Adam 3", "Inny 1")

first.run()
second.run()

third.third_run()
third.run()