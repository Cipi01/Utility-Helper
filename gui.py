from EONgaz.main import get_data_gaz
from Electrica.main import get_data_el
import PySimpleGUI as sg
from funcs import g_text_to_month, e_text_to_month, index_status

USERNAME = "andreeamarian24@yahoo.it"
PASS = "Baritiu109a"
#TODO: Make additional gui for log in(Username+pass) which will be saved after

data_g = get_data_gaz()
data_e = get_data_el()


if data_e[3] != 'Nu sunt facturi de plata' and data_e[4] != 'Nu sunteti in perioada de autocitire.':
    filtered_data_e = [f"{data_e[-1]} lei", data_e[4]]

else:
    filtered_data_e = ['No $', 'No data']

gaz_index_date = g_text_to_month(data_g)
electric_index_date = e_text_to_month(data_e)

status_gaz = index_status(gaz_index_date)
status_el = index_status(electric_index_date)
if status_gaz == "În perioada auto-citirii" or status_el == "În perioada auto-citirii":
    print("Reached GUi to show")
    # Start GUI
    sg.theme('DarkAmber')
    layout = [
        [sg.Titlebar('Welcome to the Index reminder program!')],
        [sg.Text(f"Natural gas status: {status_gaz}")],
        [sg.Text(f"Electricity status: {status_el}")],
        [sg.Button('Exit')]
    ]
    window = sg.Window('Window Title', layout, element_justification='center')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

    window.close()
