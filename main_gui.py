
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import speech_recognition as sr
from playsound import playsound
from pathlib import Path
from tkinter import END, RIGHT, LEFT, Tk, NORMAL, DISABLED, Canvas, Entry, Text, Button, PhotoImage, StringVar, ttk
from functions import update_config, clean_cookies
import sv_ttk
from settings_gui import launch_settings_window, config_data
import keyboard
from time import sleep
import json
import keyboard
import os
import requests
from pathlib import Path

FONT = ("RobotoItalic ExtraBold", 18 * -1)
ASSETS_PATH = Path.cwd() / 'build' / 'assets' / 'frame1'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



# ------------- Global Variables ------------- #
current_nomi = config_data['default_nomi']
play_sound = config_data['record_sound']
nomi_options = [nomi['name'] for nomi in config_data['nomis']]
status = "Not Connected"
chat_text = ''
driver = None
recording_sound = str(relative_to_assets("notification.wav"))

def update_gui_status(new_status):
    global status
    canvas.itemconfig(status_text, text=new_status)
    window.update_idletasks()
    
def update_text(sender, message):
    # Enable the widget, update the text, and then disable it again
    chat_box.config(state=NORMAL)
    tag = "sender1" if sender == "Sender1" else "sender2"
    chat_box.insert(END, f"{message}\n", tag)
    chat_box.config(state=DISABLED)
    chat_box.see(END)

# ------------------------------ Selenium Setup ------------------------------ #

def launch_selenium():
    global driver, status
    cookies = clean_cookies(config_data['cookies'])
    profile_path = webdriver.FirefoxProfile(config_data['ff_profile_url'])
    options = Options()
    options.add_argument("-headless") 
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.profile = profile_path

    update_gui_status("Connecting...")
    
    driver = webdriver.Firefox(options=options)
    
    # Navigate to main domain
    driver.get("https://nomi.ai")

    # Load the main domain cookies
    print(cookies)
    main_domain_cookies = [cookie for cookie in cookies if cookie["domain"] == ".nomi.ai"]
    for cookie in main_domain_cookies:
        driver.add_cookie(cookie)

    # Navigate to the subdomain
    driver.get("https://beta.nomi.ai/sign-in")

    # Load the subdomain cookies
    subdomain_cookies = [cookie for cookie in cookies if cookie["domain"] == "beta.nomi.ai"]
    for cookie in subdomain_cookies:
        driver.add_cookie(cookie)

    # Navigate to desired Nomi page
    driver.get(f"https://beta.nomi.ai/nomis/{current_nomi['nomi_id']}")
    
    update_gui_status("Connected!")
    
    last_message = driver.find_elements(By.CLASS_NAME, "css-2hr7pt")[-1].text
    update_text("Sender2", last_message)
    

def update_driver():
    driver.get(f"https://beta.nomi.ai/nomis/{current_nomi['nomi_id']}")
    last_message = driver.find_elements(By.CLASS_NAME, "css-2hr7pt")[-1].text
    update_text("Sender2", last_message)
    
   
# ------------- Speech Recording ------------- #

recognizer = sr.Recognizer()
mic = sr.Microphone()

def start_recording():
    if config_data['record_sound']:
        playsound(recording_sound)
    handle_mic_input()

def recognize_speech():
    with mic as source:
      update_gui_status("Recording...")
      
      audio_data = recognizer.listen(source)
      update_gui_status("Converting user input...")
      
      # Use SpeechRecognition to convert audio to text
      try:
         text = recognizer.recognize_google_cloud(audio_data, credentials_json=config_data['cloud_credentials'])
         update_text("Sender1", text)
         return text
      except sr.UnknownValueError:
         return "Could not understand audio"
      except sr.RequestError as e:
         return f"Could not request results; {e}"


def handle_mic_input():
    message = recognize_speech()
    send_message_through_selenium(message)
    
    
# Selenium interaction with chat text box
def send_message_through_selenium(message):
   chat_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/form/div[1]/textarea')
   ActionChains(driver)\
      .send_keys_to_element(chat_box, message)\
      .send_keys(Keys.ENTER)\
      .perform()
 
   # Keeps track of last response and triggers speech response when new response is received 
   last_response = driver.find_elements(By.CLASS_NAME, "css-2hr7pt")[-1].text
   is_waiting = True
   
   update_gui_status("Awaiting Nomi response...")

   while is_waiting:
      sleep(.5)
      new_response = driver.find_elements(By.CLASS_NAME, "css-2hr7pt")[-1].text
      if new_response != last_response:
         is_waiting = False
         last_response = new_response
         update_text("Sender2", new_response)
         text_to_speech_via_elevenlabs(new_response)
    
# ------------- Speech Response ------------- #


# Text to Speech (for ElevenLabs)
def text_to_speech_via_elevenlabs(text):
   
   el_endpoint = f'https://api.elevenlabs.io/v1/text-to-speech/{current_nomi["voice_id"]}'
   el_api = config_data['eleven_api'] 
   
   update_gui_status("Voice conversion in progress...")
   
   headers = {'accept': '*/*', 'xi-api-key': el_api, 'Content-Type': 'application/json'}
   data = json.dumps({"model_id": current_nomi['model_id'], "text": text, "stability": current_nomi['stability'], "similarity_boost": current_nomi['similarity_boost'], "style": current_nomi['style'], "use_speaker_boost": current_nomi['speaker_boost']})

   response = requests.post(url=el_endpoint, headers=headers, data=data)
   
   update_gui_status("Audio received successfully!")
   
   with open('response.mp3', 'wb') as f:
      f.write(response.content)

   playsound('response.mp3')
   os.remove('response.mp3')
   


# ------------------------------ Main GUI ------------------------------ #


def defocus_main(event):
    event.widget.master.focus_set()
    
window = Tk()
window.title('Nomi Talk')
window.geometry("982x505")
window.configure(bg = "#202020")
sv_ttk.set_theme("dark")

canvas = Canvas(
    window,
    bg = "#202020",
    height = 505,
    width = 982,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


# ------------- Button Connect ------------- #

button_image_5 = PhotoImage(
    file=relative_to_assets("button_connect.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=launch_selenium,
    relief="flat"
)
button_5.place(
    x=28.0,
    y=22.0,
    width=40.0,
    height=40.0
)


# ------------- Status Bar ------------- #

status_text = canvas.create_text(
    106.0,
    40.0,
    anchor="nw",
    text=status,
    fill="#FFFFFF",
    font=("RobotoItalic SemiBold", 14 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    209.0,
    37.0,
    image=image_image_6
)


# ------------- NT Title ------------- #

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    491.0,
    36.0,
    image=image_image_5
)


# ------------- Button Recording Sound ------------- #

def sound_toggle():
    if play_sound:
        button_sound.config(image=button_image_3)
    else:
        button_sound.config(image=button_image_4)
        window.update_idletasks()
 
def set_sound():
    global play_sound
    if play_sound:
        play_sound = False
        sound_toggle()
    else:
        play_sound = True
        sound_toggle()
    config_data['record_sound'] = play_sound
    update_config(config_data)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_sound = Button(
    borderwidth=0,
    highlightthickness=0,
    command=set_sound,
    relief="flat"
)
sound_toggle()
button_sound.place(
    x=664.0,
    y=24.0,
    width=45.0,
    height=22.0
)

canvas.create_text(
    714.0,
    27.0,
    anchor="nw",
    text="Play Recording Sound?",
    fill="#FFFFFF",
    font=("Roboto Regular", 14 * -1)
)


# ------------- Button Settings ------------- #

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: launch_settings_window(window),
    relief="flat"
)
button_2.place(
    x=929.0,
    y=21.0,
    width=30.0,
    height=30.0
)


# ------------- Select Nomi ------------- #

def update_nomi(event):
    nomi_name = nomi_selection.get()
    for nomi in config_data['nomis']:
        if nomi_name in nomi['name']:
            config_data['default_nomi'] = nomi
            update_config(config_data)
            chat_box.config(state=NORMAL)  # Enable the text widget to modify it
            chat_box.delete("1.0", END)    # Delete all the content
            chat_box.config(state=DISABLED)
        
    

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    180.48077392578125,
    110.0,
    image=image_image_4
)

nomi_selection = StringVar()

recta_x1, recta_y1, recta_x2, recta_yb = 31.48077392578125, 102.0, 329.48077392578125, 136.0
canvas.create_rectangle(
    recta_x1,
    recta_y1,
    recta_x2,
    recta_yb,
    fill="#2D2D2D",
    outline="")

nomi_box = ttk.Combobox(
    window, 
    textvariable=nomi_selection,  
    values=nomi_options,
    style='TCombobox')
if current_nomi:
    nomi_box.set(current_nomi['name'])

recta_width = recta_x2 - recta_x1
recta_height = recta_yb - recta_y1   
nomi_box.config(width=int(recta_width / 10))
canvas.create_window(recta_x1, 
                    recta_y1, 
                    anchor='nw', 
                    window=nomi_box, 
                    width=recta_width, 
                    height=recta_height)

def update_listbox():
    nomi_box['values'] = [nomi['name'] for nomi in config_data['nomis']]

nomi_box.bind("<<ComboboxSelected>>", defocus_main)
nomi_box.bind("<<ComboboxSelected>>", update_nomi, add="+")
nomi_box.bind("<<ComboboxSelected>>", update_listbox, add="+")



# ------------- Select Keyboard Shortcut ------------- #

canvas.create_rectangle(
    349.48077392578125,
    100.0,
    541.4807739257812,
    140.0,
    fill="#2D2D2D",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    445.48077392578125,
    110.0,
    image=image_image_3
)


# ------------- Select Input Device ------------- #

canvas.create_rectangle(
    558.4807739257812,
    100.0,
    750.4807739257812,
    140.0,
    fill="#2D2D2D",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    654.4807739257812,
    110.0,
    image=image_image_2
)


# ------------- Button Talk ------------- #

def initiate_recording(event):
    if event == 'record_start':
        start_recording()
    elif event.name == 'space' and keyboard.is_pressed('ctrl+shift'):
        start_recording()
    
keyboard.on_press(initiate_recording)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: initiate_recording('record_start'),
    relief="flat"
)
button_1.place(
    x=767.4807739257812,
    y=96.0,
    width=186.0,
    height=47.0
)


# ------------- Chat Box ------------- #

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    491.0,
    319.0,
    image=image_image_1
)


canvas.create_rectangle(
    37,
    185,
    944,
    473,
    fill="#4D294E",
    outline="")

chat_box = Text(window, selectbackground="#4D294E", bg="#4D294E", borderwidth=0, highlightthickness=0)
scroll_bar = ttk.Scrollbar(window, command=chat_box.yview)
scroll_bar.place(x=930, y=185, width=20, height=288)
chat_box.config(yscrollcommand=scroll_bar.set)
chat_box.config(state=DISABLED)

chat_box.tag_configure("sender1", foreground="white", justify=RIGHT)
chat_box.tag_configure("sender2", foreground="#F35CF6", justify=LEFT)

canvas.create_window(37, 
                    185, 
                    anchor='nw', 
                    window=chat_box, 
                    width=900, 
                    height=288)

canvas.create_text(
    37.0,
    191.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("RobotoRoman ExtraBold", 18 * -1)
)

window.resizable(False, False)
window.mainloop()




