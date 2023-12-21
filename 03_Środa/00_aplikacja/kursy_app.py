import PySimpleGUI as sg
from functions.nbp_operations import get_values
from functions.wykres import plotting
from functions.markdown import mdcreate
from functions.docx import docxcreate

# logowanie zdarzeń
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler = logging.FileHandler('kursy.log')
handler.setFormatter(formatter)
logger.addHandler(handler)
##############################


layout = [
    [sg.Text('Sprawdzimy kursu waluty'), sg.Combo(['EUR', 'USD', 'CHF'])],
    [sg.Input(key="DATA", enable_events=True, readonly=True, size=(15,1)), sg.CalendarButton("Calendar", target="DATA", format="%Y-%m-%d", size=15)],
    [sg.Text('Ile dni wstecz (max 14)'), sg.InputText(size=(5,1))],
    [sg.Text('Nazwa pliku: png,md,docx'), sg.InputText(size=(15,1))],
    [sg.Text("-----------------------------------------------")],
    [sg.Output(size=(50, 6), key="-OUTPUT-")],
    [sg.Button('Ok'), sg.Button('KONIEC')]
         ]

window = sg.Window('Aplikacja tworząca wykres waluty', layout)

logger.debug('START')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'KONIEC':  # if user closes window or clicks cancel
        break

    if event == "Ok":
        logger.debug("Wywołanie get values")
        currency_values = get_values(values[0], values["DATA"], values[1])
        title = f"Wykres kursów waluty {values[0]} z {values[1]} dni przed {values['DATA']}"
        # print(title, currency_values, type(currency_values))
        filename = values[2]
        legenda_wykres = f"Waluta {values[0]}"
        leg_x, leg_y = "Legenda X", "Legenda Y"
        logger.debug("Wywołanie plotting")
        plotting(title, currency_values, legenda_wykres, leg_x, leg_y, filename=f"{filename}.png")
        logger.debug("Wywołanie mdcreate")
        mdcreate(legenda_wykres, values['DATA'], currency_values, filename, picture=f"{filename}.png" )
        logger.debug("Wywołanie docxcreate")
        docxcreate(filename)

logger.debug("KONIEC APP")
window.close()