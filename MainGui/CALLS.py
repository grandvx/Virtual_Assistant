
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Users/ilias/Desktop/CALLS&SMS/build/assets_7/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

PhoneNumber = []

def Button12():
    PhoneNumber.append('1')
    entry_1.insert(tk.END,"1")
def Button11():
    PhoneNumber.append('2')
    entry_1.insert(tk.END,"2")
def Button10():
    PhoneNumber.append('3')
    entry_1.insert(tk.END,"3")
def Button9():
    PhoneNumber.append('4')
    entry_1.insert(tk.END,"4")
def Button8():
    PhoneNumber.append('5')
    entry_1.insert(tk.END,"5")
def Button7():
    PhoneNumber.append('6')
    entry_1.insert(tk.END,"6")
def Button6():
    PhoneNumber.append('7')
    entry_1.insert(tk.END,"7")
def Button5():
    PhoneNumber.append('8')
    entry_1.insert(tk.END,"8")
def Button4():
    PhoneNumber.append('9')
    entry_1.insert(tk.END,"9")
def Button2():
    PhoneNumber.append('0')
    entry_1.insert(tk.END,"0")
def Button3():
    PhoneNumber.append('*')
    entry_1.insert(tk.END,"*")
def Button1():
    PhoneNumber.append('#')
    entry_1.insert(tk.END,"#")

def Call():
    for item in PhoneNumber:
        if PhoneNumber[0]=='6' and PhoneNumber[1]=='9':
            print(PhoneNumber)
            messagebox.showinfo(message="The contact has been called")
            entry_1.delete('1.0',tk.END)
            break
        else:
            print(PhoneNumber)
            messagebox.showerror(message="There is no Contact with this number")
            entry_1.delete('1.0',tk.END)
            break
    PhoneNumber.clear()
    print(PhoneNumber)

    
def TakeACall():
    window = tk.Toplevel()

    window.geometry("526x600")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
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
        600.0,
        fill="#517179",
        outline="")

    canvas.create_rectangle(
        0.0,
        277.0,
        526.0,
        600.0,
        fill="#1A1F1D",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        262.5,
        147.5,
        image=entry_image_1
    )
    global entry_1
    entry_1 = Text(canvas,
        bd=0,
        bg="#517279",
        fg="#000716",
        highlightthickness=0,
        font=("Comfortaa Regular", 30 * -1)
    )
    entry_1.place(
        x=15.0,
        y=118.0,
        width=495.0,
        height=57.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        526.0,
        77.0,
        fill="#326873",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Button1,
        relief="flat"
    )
    button_1.place(
        x=381.0,
        y=518.0,
        width=110.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Button2,
        relief="flat"
    )
    button_2.place(
        x=200.0,
        y=518.0,
        width=110.0,
        height=55.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(canvas,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=Button3,
        relief="flat"
    )
    button_3.place(
        x=15.0,
        y=518.0,
        width=110.0,
        height=55.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(canvas,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=Button4,
        relief="flat"
    )
    button_4.place(
        x=381.0,
        y=448.0,
        width=110.0,
        height=55.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(canvas,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=Button5,
        relief="flat"
    )
    button_5.place(
        x=200.0,
        y=448.0,
        width=110.0,
        height=55.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(canvas,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=Button6,
        relief="flat"
    )
    button_6.place(
        x=15.0,
        y=449.0,
        width=110.0,
        height=55.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(canvas,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=Button7,
        relief="flat"
    )
    button_7.place(
        x=381.0,
        y=374.0,
        width=110.0,
        height=55.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(canvas,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=Button8,
        relief="flat"
    )
    button_8.place(
        x=200.0,
        y=374.0,
        width=110.0,
        height=55.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(canvas,
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=Button9,
        relief="flat"
    )
    button_9.place(
        x=15.0,
        y=374.0,
        width=110.0,
        height=55.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(canvas,
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=Button10,
        relief="flat"
    )
    button_10.place(
        x=381.0,
        y=300.0,
        width=110.0,
        height=55.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(canvas,
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=Button11,
        relief="flat"
    )
    button_11.place(
        x=200.0,
        y=297.0,
        width=110.0,
        height=55.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(canvas,
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=Button12,
        relief="flat"
    )
    button_12.place(
        x=15.0,
        y=300.0,
        width=110.0,
        height=55.0
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(canvas,
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=Call,
        relief="flat"
    )
    button_13.place(
        x=218.0,
        y=203.0,
        width=88.0,
        height=67.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        263.0,
        38.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()

