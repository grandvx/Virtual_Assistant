from pathlib import Path
from calendarManagement import AppointmentManager
from reminders import ReminderManager
from toDoList import TodoListManager
from player import MusicPlayer
from settings import DeviceSettings
from weather import WeatherApp
from Eshops import Eshops
from Contacts import Contacts_Win
from Mail import Mail
from CALLSSMS import CALLSMS
import subprocess

import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C://Users/keray/Unity3d/Interactionhuman/Virtual_Assistant/MainGui/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def OpenPDF():
    subprocess.Popen('lelekas',shell=True)

def Gui_Menu():
    Menu = tk.Toplevel()

    Menu.geometry("526x600")
    Menu.configure(bg = "#FFFFFF")


    canvas = Canvas(
        Menu,
        bg = "#FFFFFF",
        height = 600,
    width = 526,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        526.0,
        80.0,
        fill="#24477C",
        outline="")

    canvas.create_text(
        11.0,
        15.0,
        anchor="nw",
        text="Buttons Menu",
        fill="#3C8C6F",
        font=("MontserratRoman SemiBold", 32 * -1)
    )

    canvas.create_rectangle(
        0.0,
        80.0,
        526.0,
        601.0,
        fill="#133B40",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("Robot.png"))
    image_1 = canvas.create_image(
        264.0,
        500.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("Calendar.png"))
    button_1 = Button(canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: open_appointment_manager(),
        relief="groove"
    )
    button_1.place(
        x=20.0,
        y=101.0,
        width=110.0,
        height=48.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("List.png"))
    button_2 = Button(canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_to_do_list(),
        relief="flat"
    )
    button_2.place(
        x=206.0,
        y=174.0,
        width=110.0,
        height=48.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("Alarm.png"))
    button_3 = Button(canvas,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_reminder_manager(),
        relief="flat"
    )
    button_3.place(
        x=388.0,
        y=101.0,
        width=110.0,
        height=48.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(canvas,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=CALLSMS,
        relief="flat"
    )
    button_4.place(
        x=22.0,
        y=174.0,
        width=110.0,
        height=48.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(canvas,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=Contacts_Win,
        relief="flat"
    )
    button_5.place(
        x=388.0,
        y=173.0,
        width=116.0,
        height=48.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(canvas,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:open_weather_app(),
        relief="flat"
    )
    button_6.place(
        x=20.0,
        y=249.0,
        width=110.0,
        height=48.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(canvas,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_music_player(),
        relief="flat"
    )
    button_7.place(
        x=206.0,
        y=250.0,
        width=110.0,
        height=48.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(canvas,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_settings(),
        relief="flat"
    )
    button_8.place(
        x=389.0,
        y=250.0,
        width=110.01295471191406,
        height=48.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(canvas,
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=Eshops,
        relief="flat"
    )
    button_9.place(
        x=23.0,
        y=330.0,
        width=110.0,
        height=48.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(canvas,
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=open_google_maps,
        relief="flat"
    )
    button_10.place(
        x=206.0,
        y=329.0,
        width=110.0,
        height=48.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(canvas,
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=open_news,
        relief="flat"
    )
    button_11.place(
        x=391.0,
        y=330.0,
        width=110.0,
        height=48.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(canvas,
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=open_google,
        relief="flat"
    )
    button_12.place(
        x=78.0,
        y=410.0,
        width=110.0,
        height=48.0
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(canvas,
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=Mail,
        relief="flat"
    )
    button_13.place(
        x=206.0,
        y=103.0,
        width=111.23287963867188,
        height=48.0
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(canvas,
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_14 clicked"),
        relief="flat"
    )
    button_14.place(
        x=322.0,
        y=411.0,
        width=110.0,
        height=48.0
    )
    Menu.resizable(False, False)
    Menu.mainloop()
   
def open_appointment_manager():
    root = tk.Toplevel()
    app = AppointmentManager(root)   

def open_reminder_manager():
    root = tk.Toplevel()
    app = ReminderManager(root)    

def open_to_do_list():
    root = tk.Toplevel()
    app = TodoListManager(root)    

def open_music_player():
    root = tk.Toplevel()
    app = MusicPlayer(root)    

def open_settings():
    root = tk.Toplevel()
    app = DeviceSettings(root)

def open_weather_app():
    root = tk.Toplevel()
    app = WeatherApp(root)

def open_google_maps():
    webbrowser.open("https://www.google.com/maps")    

def open_skroutz():
    webbrowser.open("https://www.skroutz.gr")

def open_google():
    webbrowser.open("https://www.google.com")

def open_news():
    webbrowser.open("https://news.google.com/home?hl=el&gl=GR&ceid=GR:el")