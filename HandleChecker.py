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
            [sg.Checkbox('FaceBook', key='FaceBook', font=("Monospace", 20))],
            [sg.Checkbox('Instagram', key='Instagram', font=("Monospace", 20))],
            [sg.Checkbox('TikTok', key='TikTok', font=("Monospace", 20))],
        ], vertical_alignment='center', justification='center'),

        sg.Column([
            [sg.Checkbox('Pinterest', key='Pinterest', font=("Monospace", 20))],
            [sg.Checkbox('YouTube', key='YouTube', font=("Monospace", 20))],
            [sg.Checkbox('Twitch', key='Twitch', font=("Monospace", 20))],
        ], vertical_alignment='center', justification='center'),
    ],
    [sg.Text("Enter handle:", size=(20, 1), justification='center', pad=((0, 0), (10, 0)), font=("Monospace", 14))],
    [sg.Input(size=(25, 2), key='textbox', justification='center', font=("Monospace", 16))],
    [sg.Button("Search", button_color='white', pad=((0, 0), (15,10)), font=("Monospace", 20))],

    [
        sg.Column([
            [sg.Text('FaceBook:', font=("Monospace", 20)), sg.Text('', key='result_FaceBook', font=("Monospace", 20))],
            [sg.Text('Instagram:', font=("Monospace", 20)), sg.Text('', key='result_Instagram', font=("Monospace", 20))],
            [sg.Text('TikTok:', font=("Monospace", 20)), sg.Text('', key='result_TikTok', font=("Monospace", 20))],
            [sg.Text('Pinterest:', font=("Monospace", 20)), sg.Text('', key='result_Pinterest', font=("Monospace", 20))],
            [sg.Text('YouTube:', font=("Monospace", 20)), sg.Text('', key='result_YouTube', font=("Monospace", 20))],
            [sg.Text('Twitch:', font=("Monospace", 20)), sg.Text('', key='result_Twitch', font=("Monospace", 20))],
        ], vertical_alignment='center', justification='left'),
    ],
    
]

window = sg.Window("HandleChecker", layout, size=(300,465), element_justification='center')





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
    result_key = f'result_{key}'
    if key != 'textbox':
        if checkhandle(handle, key):
            window[result_key].update('✓')
        else:
            window[result_key].update('✗')

            


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    for key, selected in values.items():
        if selected:
            print_selected(key)


window.close()
exit()