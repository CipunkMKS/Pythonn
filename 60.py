import PySimpleGUI as sg

layout = [[sg.Button('Klik Saya')]]

window = sg.window('Contoh program PySimpleGUi', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
       break 
    elif event == 'klik saya':
        print('Tombol diklik')

window.close()