import PySimpleGUI as sg



layout = [
    [sg.Text('Sprawdzimy kursu waluty'), sg.Combo(['EUR', 'USD', 'CHF'])],
    [sg.Input(key="DATA", enable_events=True, readonly=True), sg.CalendarButton("Calendar", target="DATA", format="%Y-%m-%d")],
    [sg.Text('Ile dni wstecz (max 14)'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('KONIEC')]
         ]

window = sg.Window('Aplikacja tworząca wykres waluty', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'KONIEC':  # if user closes window or clicks cancel
        break

    print(values)



window.close()