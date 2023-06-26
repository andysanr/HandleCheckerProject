import PySimpleGUI as sg
import requests
import time

sg.theme("default1")

base_urls = {
     'FaceBook': 'https://www.facebook.com/',
     'Instagram': 'https://www.instagram.com/',
     'TikTok': 'https://www.tiktok.com/@',

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
        ], vertical_alignment='center', justification='center'),

        sg.Column([
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

def checkhandle(handle, key):
    url = base_urls[key] + handle   
    response = requests.get(url)
    page_content = response.text

    if key == 'Tiktok' and '"uniqueid":"' in page_content.lower():
         return False
    if key == 'FaceBook' and 'return false;' in page_content.lower():
         return True
    if key == 'Instagram' and '"pageid":"httperrorpage"' in page_content.lower():
         return True
    if key == 'Pinterest' and 'user not found' in page_content.lower():
         return True
    if key == 'Twitch' and 'href="https://www.twitch.tv/' not in page_content.lower():
         return True
    elif response.status_code == 200:
        if handle.lower() in page_content.lower():
                   return False
        elif handle.lower() not in page_content.lower():
             return True
    elif response.status_code == 404:
         time.sleep(1)
         response = requests.get(url)
         if response.status_code == 404 or handle.lower() not in page_content.lower(): 
            return True
    else:
         return True


def print_selected(key):
    handle = values['textbox']
    if key != 'textbox':
        if checkhandle(handle, key):
            print(f"Handle '{handle}' is available on {key}")
        else:
            print(f"Handle '{handle}' is not available on {key}")

            


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    for key, selected in values.items():
        if selected:
            print_selected(key)


window.close()
exit()