import PySimpleGUI as sg
import requests

sg.theme("default1")

# Define the base URLs for each social media platform
base_urls = {
    'FaceBook': 'https://www.facebook.com/',
    'Instagram': 'https://www.instagram.com/',
    'TikTok': 'https://www.tiktok.com/@',
    'Twitter': 'https://twitter.com/',
    'Reddit': 'https://www.reddit.com/user/',
    'Pinterest': 'https://www.pinterest.com/',
    'YouTube': 'https://www.youtube.com/user/',
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
        ], vertical_alignment='center', justification='center')
    ],
    [sg.Text("", size=(20, 1), justification='center')],
    [sg.Text("Enter handle", size=(20, 1), justification='center')],
    [sg.Input(size=(25, 2), key='textbox', justification='center')],
    [sg.Text("", size=(20, 1), justification='center')],
    [sg.Button("Search", button_color=('white', 'blue'), size=(10, 1), key='Search')],
]

window = sg.Window("HandleChecker", layout, size=(400, 250), element_justification='center')

def check_handle_availability(handle, platform):
    # Construct the URL for the given social media platform
    url = base_urls[platform] + handle

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the handle is available or already taken based on the response status code
    if response.status_code == 404:
        return True  # Handle is available
    else:
        return False  # Handle is already taken

def print_selected(key):
    if key != 'textbox':
        handle = values['textbox']
        is_available = check_handle_availability(handle, key)
        if is_available:
            print("Handle available on {}: {}".format(key, handle))
        else:
            print("Handle already taken on {}: {}".format(key, handle))

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
