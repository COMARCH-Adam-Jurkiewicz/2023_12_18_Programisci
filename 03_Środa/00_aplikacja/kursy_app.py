import PySimpleGUI as sg
from time import sleep
from functions.nbp_operations import get_values
from functions.wykres import plotting



layout = [
    [sg.Text('Sprawdzimy kursu waluty'), sg.Combo(['EUR', 'USD', 'CHF'])],
    [sg.Input(key="DATA", enable_events=True, readonly=True), sg.CalendarButton("Calendar", target="DATA", format="%Y-%m-%d")],
    [sg.Text('Ile dni wstecz (max 14)'), sg.InputText()],
    [sg.Text("-----------------------------------------------")],
    [sg.Output(size=(50, 6), key="-OUTPUT-")],
    [sg.Button('Ok'), sg.Button('KONIEC')]
         ]

window = sg.Window('Aplikacja tworząca wykres waluty', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'KONIEC':  # if user closes window or clicks cancel
        break

    if event == "Ok":
        currency_values = get_values(values[0], values["DATA"], values[1])
        title = f"Wykres kursów waluty {values[0]} z {values[1]} dni przed {values['DATA']}"
        sleep(10)
        print(title, currency_values, type(currency_values))
        # plotting(title, currency_values,)








window.close()