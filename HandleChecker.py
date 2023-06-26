import PySimpleGUI as sg
import requests
import time

sg.theme("default1")
# links
# https://www.facebook.com/
# https://www.instagram.com/
# https://www.tiktok.com/@
# https://www.twitter.com/
# https://www.pinterest.com/
# https://www.youtube.com/@
# https://www.twitch.tv/

# status 200 list: all ok and have username displayed (unavailable to use)
# https://www.facebook.com/LeBron
# https://www.instagram.com/elonmusk
# https://www.tiktok.com/@elonmusk
# https://www.twitter.com/elonmusk
# https://www.pinterest.com/elonmusk
# https://www.youtube.com/@elonmusk
# https://www.twitch.tv/elonmusk

# doesn't exist : 
# https://www.facebook.com/Leon52k0235      status 200, message: 
                                            # This content isn't available right now
                                            # When this happens, it's usually because 
                                            # the owner only shared it with a small 
                                            # group of people, changed who can see 
                                            # it or it's been deleted.

# https://www.instagram.com/Leon52k0235     status 200, message:
                                            # Sorry, this page isn't available.
                                            # The link you followed may be broken, 
                                            # or the page may have been removed. 
                                            # Go back to Instagram.

# https://www.tiktok.com/@Leon52k0235       status 200, message:
                                            # Couldn't find this account
                                            # Looking for videos? Try browsing 
                                            # our trending creators, hashtags, and sounds.

# https://www.twitter.com/Leon52k0235       status 200, message:
                                            #This account doesn’t exist
                                            #Try searching for another.

# https://www.pinterest.com/Leon52k0235     status 200, message:
                                            # (no message)


# https://www.youtube.com/@Leon52k0235      status 404, message:
                                            #This page isn't available. Sorry about that.
                                            #Try searching for something else.

# https://www.twitch.tv/Leon52k0235         status 200, message:
                                            #Sorry. Unless you’ve got a time machine, 
                                            # that content is unavailable.






base_urls = {
     'FaceBook': 'https://www.facebook.com/',
     'Instagram': 'https://www.instagram.com/',
     'TikTok': 'https://www.tiktok.com/@',
     'Twitter': 'https://www.twitter.com/',

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