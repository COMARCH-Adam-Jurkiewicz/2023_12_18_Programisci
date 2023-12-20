import snakemd

def mdcreate(title: str, finish_date: str, values: list[float], filename: str="wykres", picture: str="wykres.png"):
    doc = snakemd.new_doc()
    doc.add_heading("Kurs Waluty z dnia.", 3)
    doc.add_horizontal_rule()
    doc.add_block(snakemd.Paragraph([snakemd.Inline("Wykres", image=picture)]))
    doc.dump(filename)




if __name__ == "__main__":
    mdcreate("TEST", "2023-12-31", [3.14, 4.12, 2.99])

