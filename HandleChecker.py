import PySimpleGUI as sg
import os.path

sg.theme("default1")

layout = [
    [sg.Checkbox('FaceBook', key='FaceBook')],
    [sg.Checkbox('Instagram', key='Instagram')],
    [sg.Checkbox('TikTok', key='TikTok')],
    [sg.Checkbox('Twitter', key='Twitter')],
    [sg.Checkbox('Reddit', key='Reddit')],
    [sg.Checkbox('Pinterest', key='Pinterest')],
    [sg.Checkbox('YouTube', key='YouTube')],
    [sg.Checkbox('Twitch', key='Twitch')],
    [sg.Text("Enter handle",size=(20,1))],
    [sg.Input(size=(25, 2), key='textbox')],
    [sg.Button("Search")],
]

window = sg.Window("HandleChecker", layout, size=(300,250))

def print_selected(key):
        if key != 'textbox':
            print("User selected: " + key)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    for key, selected in values.items():
        if selected:
            print_selected(key)

    if event == "Search":
        print("User selected search")

window.close()
exit()