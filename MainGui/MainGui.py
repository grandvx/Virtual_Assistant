from Menu import Gui_Menu
from pathlib import Path

import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import PyPDF2
import webbrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C://Users/keray/Unity3d/Interactionhuman/Virtual_Assistant/MainGui/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def OpenPDF():
    path = r"C:/Users/keray/Unity3d/Interactionhuman/Virtual_Assistant/User Manual PIXEL.pdf"
    subprocess.Popen([path],shell=True)

window = tk.Tk()

window.geometry("400x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    400.0,
    600.0,
    fill="#2F7470",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    200.5,
    375.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#2F615B",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=7.0,
    y=345.0,
    width=387.0,
    height=59.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    219.0,
    209.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=175.0,
    y=444.0,
    width=55.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=OpenPDF,
    relief="flat"
)
button_2.place(
    x=10.0,
    y=6.0,
    width=32.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Gui_Menu,
    relief="flat"
)
button_3.place(
    x=357.0,
    y=6.0,
    width=32.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
