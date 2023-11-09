
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Canvas, Entry, StringVar, Button, PhotoImage, filedialog, Toplevel, ttk, messagebox
from functions import load_config, update_settings, create_nomi, truncate_string
import sv_ttk


config_data = load_config()

FONT = ("RobotoItalic ExtraBold", 18 * -1)
ASSETS_PATH = Path.cwd() / 'build' / 'assets' / 'frame1'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def launch_settings_window(main):

    settings_window = Toplevel()
    settings_window.title('Settings')
    settings_window.geometry("450x645")
    settings_window.configure(bg = "#202020")
    settings_window.transient(main)
    settings_window.grab_set()
    settings_window.focus_set()
    
    sv_ttk.set_theme("dark")

    def defocus_settings(event):
        event.widget.master.focus_set()

    settings_canvas = Canvas(
        settings_window,
        bg = "#202020",
        height = 645,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    settings_canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("sw_image_1.png"))
    image_1 = settings_canvas.create_image(
        229.0,
        482.0,
        image=image_image_1
    )


    # ------------- Settings Title ------------- #

    image_image_6 = PhotoImage(
        file=relative_to_assets("sw_image_6.png"))
    image_6 = settings_canvas.create_image(
        225.0,
        37.0,
        image=image_image_6
    )


    # ------------- Button Info ------------- #

    ## TODO

    button_image_8 = PhotoImage(
        file=relative_to_assets("sw_button_8.png"))
    button_8 = Button(
        settings_window,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=20.0,
        y=21.0,
        width=30.0,
        height=30.0
    )




    def select_file(source):
        nonlocal cookie_path, ff_profile_path, google_cloud_api
        if source == 'cookies':
            file_path = filedialog.askopenfilename()
            if file_path:
                cookie_path = file_path
                settings_canvas.itemconfig(cookies_text, 
                                text=truncate_string(cookie_path, 40))
        elif source == 'firefox':
            file_path = filedialog.askdirectory()
            if file_path:
                ff_profile_path = file_path
                settings_canvas.itemconfig(firefox_text, 
                                text=truncate_string(ff_profile_path, 40))
        elif source == 'google':
            file_path = filedialog.askopenfilename()
            if file_path:
                google_cloud_api = file_path
                settings_canvas.itemconfig(google_text, 
                                text=truncate_string(google_cloud_api, 40))

        settings_window.update_idletasks()

    def create_file_dialog_button(source):
        button = Button(settings_window, command=lambda: select_file(source))
        return button

    # ------------- Cookies Field and Button ------------- #

    cookie_path = config_data["cookies"]

    image_image_5 = PhotoImage(
        file=relative_to_assets("sw_image_5.png"))
    image_5 = settings_canvas.create_image(
        229.0,
        100.0,
        image=image_image_5
    )

    cookies_text = settings_canvas.create_text(
        41.0,
        101.0,
        anchor="nw",
        text=truncate_string(config_data["cookies"], 40),
        fill="#939393",
        font=("RobotoItalic ExtraBold", 18 * -1)
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("sw_button_7.png"))
    button_cookies = create_file_dialog_button(
        'cookies'
    )
    button_cookies.config(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
        )
    button_cookies.place(
        x=400.0,
        y=103.0,
        width=16.0,
        height=16.0
    )


    # ------------- Firefox Field and Button ------------- #

    ff_profile_path = config_data['ff_profile_url']

    image_image_4 = PhotoImage(
        file=relative_to_assets("sw_image_4.png"))
    image_4 = settings_canvas.create_image(
        229.0,
        169.0,
        image=image_image_4
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("sw_button_6.png"))
    button_firefox = create_file_dialog_button(
        'firefox'
    )
    button_firefox.place(
        x=400.0,
        y=171.0,
        width=16.0,
        height=16.0
    )
    button_firefox.config(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    firefox_text = settings_canvas.create_text(
        41.0,
        169.0,
        anchor="nw",
        text=truncate_string(config_data['ff_profile_url'], 40),
        fill="#939393",
        font=("RobotoItalic ExtraBold", 18 * -1)
    )


    # ------------- Google Field and Button ------------- #

    google_cloud_api = config_data['cloud_credentials']

    image_image_3 = PhotoImage(
        file=relative_to_assets("sw_image_3.png"))
    image_3 = settings_canvas.create_image(
        229.0,
        239.0,
        image=image_image_3
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("sw_button_5.png"))
    button_google = create_file_dialog_button(
        'google'
    )
    button_google.config(
        image=button_image_5, 
        borderwidth=0, 
        highlightthickness=0,
        relief="flat"
    )
    button_google.place(
        x=400.0,
        y=241.0,
        width=16.0,
        height=16.0
    )

    google_text = settings_canvas.create_text(
        41.0,
        239.0,
        anchor="nw",
        text=truncate_string(config_data['cloud_credentials'], 40),
        fill="#939393",
        font=("RobotoItalic ExtraBold", 18 * -1)
    )


    # ------------- Eleven Labs API Field ------------- #

    el_api = config_data['eleven_api']

    image_image_2 = PhotoImage(
        file=relative_to_assets("sw_image_2.png"))
    image_2 = settings_canvas.create_image(
        156.0,
        306.0,
        image=image_image_2
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("sw_entry_5.png"))
    entry_bg_5 = settings_canvas.create_image(
        157.0,
        315.0,
        image=entry_image_5
    )
    entry_el_api = Entry(
        settings_window,
        bd=0,
        bg="#2D2D2D",
        fg="#939393",
        highlightthickness=0,
        font=FONT
    )
    entry_el_api.insert(
        0, el_api
    )
    entry_el_api.place(
        x=41.0,
        y=298.0,
        width=232.0,
        height=32.0
    )




    # ------------- Button Settings Submit ------------- #

    def submit_settings():
        nonlocal cookie_path, ff_profile_path, google_cloud_api, entry_el_api
        settings = {
            'cookies': cookie_path, 
            'ff_profile_url': ff_profile_path,
            'cloud_credentials': google_cloud_api,
            'eleven_api': entry_el_api.get()
        }
        try:
            update_settings(config_data, **settings)
            messagebox.showinfo("Settings Updated", "Settings updated successfully!")
        except:
            messagebox.showerror("Error", "Error message")
        

    button_image_4 = PhotoImage(
        file=relative_to_assets("sw_button_4.png"))
    button_submit = Button(
        settings_window,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=submit_settings,
        relief="flat"
    )
    button_submit.place(
        x=301.0,
        y=296.0,
        width=128.0,
        height=40.0
    )



    # ------------- Entry Nomi Name -----

    entry_image_4 = PhotoImage(
        file=relative_to_assets("sw_entry_4.png"))
    entry_bg_4 = settings_canvas.create_image(
        132.5,
        389.0,
        image=entry_image_4
    )
    entry_nomi_name = Entry(
        settings_window,
        bd=0,
        bg="#2D2D2D",
        fg="#939393",
        highlightthickness=0,
        font=FONT
    )
    entry_nomi_name.place(
        x=48.0,
        y=372.0,
        width=169.0,
        height=32.0
    )
    entry_nomi_name.insert(0, "Nomi's Name")


    # ------------- Entry Nomi ID ------------- #

    entry_image_3 = PhotoImage(
        file=relative_to_assets("sw_entry_3.png"))
    entry_bg_3 = settings_canvas.create_image(
        132.5,
        436.0,
        image=entry_image_3
    )
    entry_nomi_id = Entry(
        settings_window,
        bd=0,
        bg="#2D2D2D",
        fg="#939393",
        highlightthickness=0,
        font=FONT
    )
    entry_nomi_id.place(
        x=48.0,
        y=419.0,
        width=169.0,
        height=32.0
    )
    entry_nomi_id.insert(0, 'Nomi ID')


    # ------------- Entry Voice ID ------------- #

    entry_image_2 = PhotoImage(
        file=relative_to_assets("sw_entry_2.png"))
    entry_bg_2 = settings_canvas.create_image(
        132.5,
        483.0,
        image=entry_image_2
    )
    entry_voice_id = Entry(
        settings_window,
        bd=0,
        bg="#2D2D2D",
        fg="#939393",
        highlightthickness=0,
        font=FONT
    )
    entry_voice_id.place(
        x=48.0,
        y=466.0,
        width=169.0,
        height=32.0
    )
    entry_voice_id.insert(0, 'Eleven Labs Voice ID')


    # ------------- Entry Model ID ------------- #

    entry_image_1 = PhotoImage(
        file=relative_to_assets("sw_entry_1.png"))
    entry_bg_1 = settings_canvas.create_image(
        165.0,
        545.0,
        image=entry_image_1
    )
    entry_model_id = Entry(
        settings_window,
        bd=0,
        bg="#2D2D2D",
        fg="#939393",
        highlightthickness=0,
        font=FONT
    )
    entry_model_id.place(
        x=49.0,
        y=528.0,
        width=232.0,
        height=32.0
    )
    entry_model_id.insert(0, 'eleven_multilingual_v2')
    



    # ------------- Voice Settings ------------- #

    options = [i for i in range(1,101)]
    
    stability_selection = StringVar()
    rect_x1a, rect_y1a, rect_x2a, rect_y2a = 382.0, 372.0, 418.0, 406.0
    settings_canvas.create_rectangle(
        rect_x1a,
        rect_y1a,
        rect_x2a,
        rect_y2a,
        fill="#2D2D2D",
        outline=""
    )
    
    stability_box = ttk.Combobox(
        settings_window, 
        textvariable=stability_selection, 
        values=options,
        style='TCombobox')
    stability_box.set('50')
    
    recta_width = rect_x2a - rect_x1a
    recta_height = rect_y2a - rect_y1a
    stability_box.config(width=int(recta_width / 10))
    settings_canvas.create_window(rect_x1a, 
                         rect_y1a, 
                         anchor='nw', 
                         window=stability_box, 
                         width=recta_width, 
                         height=recta_height)
    stability_box.bind("<FocusIn>", defocus_settings)


    style_selection = StringVar()
    rect_x1b, rect_y1b, rect_x2b, rect_yb2 = 382.0, 426.0, 418.0, 460.0
    settings_canvas.create_rectangle(
        rect_x1b,
        rect_y1b,
        rect_x2b,
        rect_yb2,
        fill="#2D2D2D",
        outline="")
    
    style_box = ttk.Combobox(
        settings_window, 
        textvariable=style_selection,  
        values=options,
        style='TCombobox')
    style_box.set('50')
    
    rectb_width = rect_x2b - rect_x1b
    rectb_height = rect_yb2 - rect_y1b    
    style_box.config(width=int(rectb_width / 10))
    settings_canvas.create_window(rect_x1b, 
                        rect_y1b, 
                        anchor='nw', 
                        window=style_box, 
                        width=rectb_width, 
                        height=rectb_height)
    style_box.bind("<FocusIn>", defocus_settings)




    similarity_selection = StringVar()
    rect_x1c, rect_y1c, rect_x2c, rect_ybc = 382.0, 480.0, 418.0, 514.0
    settings_canvas.create_rectangle(
        rect_x1c,
        rect_y1c,
        rect_x2c,
        rect_ybc,
        fill="#2D2D2D",
        outline="")
    
    simliarity_box = ttk.Combobox(
        settings_window, 
        textvariable=similarity_selection,   
        values=options,
        style='TCombobox')
    simliarity_box.set('50')
    
    rectc_width = rect_x2c - rect_x1c
    rectc_height = rect_ybc - rect_y1c    
    simliarity_box.config(width=int(rectc_width / 10))
    settings_canvas.create_window(rect_x1c, 
                        rect_y1c, 
                        anchor='nw', 
                        window=simliarity_box, 
                        width=rectc_width, 
                        height=rectc_height)
    simliarity_box.bind("<FocusIn>", defocus_settings)


    
    
    
    button_image_2 = PhotoImage(
        file=relative_to_assets("sw_button_2.png"))
    button_image_3 = PhotoImage(
        file=relative_to_assets("sw_button_3.png"))
    def speaker_toggle():
        nonlocal is_speaker
        if is_speaker:
            is_speaker = False
            button_speaker.config(image=button_image_3)
        else:
            is_speaker = True
            button_speaker.config(image=button_image_2)
        settings_window.update_idletasks()
    
    is_speaker = False
    button_speaker = Button(
        settings_window, 
        image=None,
        borderwidth=0,
        highlightthickness=0,
        command=speaker_toggle,
        relief="flat"
    )
    button_speaker.place(
        x=388.0,
        y=533.0,
        width=24.0,
        height=24.0
    )


    def add_nomi():
        
        nomi_details = {
            'name': entry_nomi_name.get(),
            'nomi_id': entry_nomi_id.get(),
            'voice_id': entry_voice_id.get(),
            'model_id': entry_model_id.get(),
            'stability': int(stability_selection.get()),
            'style': int(style_selection.get()),
            'similarity_boost': int(similarity_selection.get()),
            'speaker_boost': is_speaker
        }
        
        try:
            create_nomi(config_data, nomi_details)
            messagebox.showinfo("Nomi Added", "Nomi has been added!")
        except:
            messagebox.showerror("Error", "Error message")


    button_image_1 = PhotoImage(
        file=relative_to_assets("sw_button_1.png"))
    button_add_nomi = Button(
        settings_window, 
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=add_nomi,
        relief="flat"
    )
    button_add_nomi.place(
        x=149.0,
        y=573.0,
        width=159.0,
        height=40.0
    )


    settings_window.resizable(False, False)
    settings_window.mainloop()