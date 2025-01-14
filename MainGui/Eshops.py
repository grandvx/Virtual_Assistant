
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import webbrowser
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C://Users/keray/Unity3d/Interactionhuman/Virtual_Assistant/MainGui/assets_2/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def McDonalds():
    webbrowser.open('https://mcdonalds.gr/')

def Amazon():
    webbrowser.open('https://www.amazon.com/')

def Walmart():
    webbrowser.open('https://www.walmart.com/')

def Addidas():
    webbrowser.open('https://www.adidas.gr/')

def Ebay():
    webbrowser.open('https://www.ebay.com/')

def Nike():
    webbrowser.open('https://www.nike.com/gr/')

def Eshops():
    window = tk.Toplevel()

    window.geometry("449x592")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 592,
        width = 449,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        449.0,
        76.0,
        fill="#3080CA",
        outline="")

    canvas.create_rectangle(
        0.0,
        76.0,
        449.0,
        592.0,
        fill="#3A626B",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("Eshops.png"))
    image_1 = canvas.create_image(
        224.0,
        38.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("Amazon.png"))
    button_1 = Button(canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Amazon,
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=140.0,
        width=100.0,
        height=47.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("walmart.png"))
    button_2 = Button(canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Walmart,
        relief="flat"
    )
    button_2.place(
        x=167.0,
        y=140.0,
        width=100.0,
        height=47.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("nike.png"))
    button_3 = Button(canvas,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=Nike,
        relief="flat"
    )
    button_3.place(
        x=304.0,
        y=140.0,
        width=100.0,
        height=47.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("Ebay.png"))
    button_4 = Button(canvas,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=Ebay,
        relief="flat"
    )
    button_4.place(
        x=167.0,
        y=232.0,
        width=100.0,
        height=47.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("addidas.png"))
    button_5 = Button(canvas,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=Addidas,
        relief="flat"
    )
    button_5.place(
        x=304.0,
        y=232.0,
        width=100.0,
        height=47.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("Mc.png"))
    button_6 = Button(canvas,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=McDonalds,
        relief="flat"
    )
    button_6.place(
        x=30.0,
        y=232.0,
        width=100.0,
        height=47.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("Robotaki.png"))
    image_2 = canvas.create_image(
        218.0,
        492.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()
