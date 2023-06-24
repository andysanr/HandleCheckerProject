import PySimpleGUI as sg
import requests

sg.theme("default1")

base_urls = {
     'FaceBook': 'https://www.facebook.com/',
     'Instagram': 'https://www.instagram.com/',
     'TikTok': 'https://www.tiktok.com/@',
     'Twitter': 'https://www.twitter.com/',

     'Reddit': 'https://www.reddit.com/user/',
     'Pinterest': 'https://www.pinterest.com/',
     'YouTube': 'https://www.youtube.com/@',
     'Twitch': 'https://www.twitch.tv/'
}

layout = [
    [
        sg.Column([
            [sg.Checkbox('FaceBook', key='FaceBook')],
            [sg.Checkbox('Instagram', key='Instagram')],
            [sg.Checkbox('TikTok', key='TikTok')],
            [sg.Checkbox('Twitter', key='Twitter')]
        ], vertical_alignment='center', justification='center'),

        sg.Column([
            [sg.Checkbox('Reddit', key='Reddit')],
            [sg.Checkbox('Pinterest', key='Pinterest')],
            [sg.Checkbox('YouTube', key='YouTube')],
            [sg.Checkbox('Twitch', key='Twitch')]
        ], vertical_alignment='center', justification='center'),
    ],
    [sg.Text("Enter handle", size=(20, 1), justification='center')],
    [sg.Input(size=(25, 2), key='textbox', justification='center')],
    [sg.Button("Search")],
]

window = sg.Window("HandleChecker", layout, size=(300,265))

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