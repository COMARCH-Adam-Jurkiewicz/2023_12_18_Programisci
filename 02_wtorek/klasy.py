class Statek:
    def __init__(self, name="Cutty Sark"):
        self.__name = name
        self._name = "Inne"

    def what_name(self):
        return self.__name


a = Statek()
print(a.what_name())
print(a._name)
a._name = "Cosik"
print(a._name)
print(a)
# error --> print(a.__name)
