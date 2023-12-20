import PySimpleGUI as sg
from functions.db_operations import *

layout = [
    [sg.Text('Some text on Row 1')],
    [sg.Text('Enter something on Row 2'), sg.InputText()],
    [sg.Text("Wybierz plik: "), sg.FileBrowse("Wybór", tooltip="Nasz pliczek z bazą JSON")],
    [sg.Text('Enter something on Row 3'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('KONIEC')]
         ]

window = sg.Window('Okno Adama', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'KONIEC':  # if user closes window or clicks cancel
        break

    print(values)
    if values["Wybór"]:
        baza = dbopen(values["Wybór"])
        print(type(baza), baza)


window.close()