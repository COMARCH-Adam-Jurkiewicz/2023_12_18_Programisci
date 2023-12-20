from tinydb import TinyDB, Query, where



def dbopen(file: str):
    try:
        db = TinyDB(file)
        return db
    except:
        return -9


if __name__ == "__main__":
    # to się wykonuje tylko przy bezpośrednim uruchomieniu
    print("TEST __maina")
    print(f"{__name__=}")
    assert dbopen("nonexist.json") == -9 , "Coś nie tak..."
else:
    print(f"Import z {__name__=}")