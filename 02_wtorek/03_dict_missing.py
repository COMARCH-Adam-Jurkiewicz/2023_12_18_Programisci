slownik = {
    "A": "Adam",
    "B": "Beata",
}

print(slownik["A"])
# print(slownik["C"])  # _missingkey_

class My_Dict_Subclass(dict):
    def __missing__(self, key):
        return f"Niestety, brak klucza: {key}"

my_dict = My_Dict_Subclass(slownik)
print(my_dict['B'])
print(my_dict['D'])
# finxter