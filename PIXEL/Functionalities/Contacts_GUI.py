
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, messagebox, Listbox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C://Users/ilias/Desktop/PIXEL/Functionalities/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


Contacts = {}
    
def Add_Contact():
    # get the text from the entries(tkinter)
    name = entry_1.get()
    phone_number = entry_2.get()
    #add them to dictionary
    Contacts[name] = phone_number
    ####Procedure for removing curly brackets {} and ''###
    dict_output = Contacts.__str__()
    dict_output = dict_output.replace('{','').replace('}','')
    for name, phone_number in Contacts.items():
        dict_output = f'{name} : {phone_number}'
    Contacts_list.insert(tk.END,dict_output)
    print(Contacts)
    #Show_Contacts()
    
def Show_Contacts():
    contacts_text = " "
    for name,phone_number in Contacts.items():
        contacts_text += f' {name} : {phone_number}\n'
    #canvas.itemconfig(item, text = contacts_text)
    #canvas.itemconfig(item, anchor = "nw")
        
def ApplyButtonInsert():
    messagebox.showinfo("Insertion", "Contact has been added succesfully")
    Add_Contact()

def Delete_Contact():

    index = Contacts_list.curselection()

    contact_info = Contacts_list.get(index)

    for name, phonenumber in Contacts.items():
        if name == contact_info:
            Contacts.pop(index)
            break

    Contacts_list.delete(index)
    print(Contacts)
    #name = delete_entry.get()
    #if name in Contacts.keys():
        #messagebox.showinfo("Deletion","Contact has been deleted succesfully")
        #Contacts.pop(name)
        #Contacts_list.delete(name)
        #Show_Contacts()
    #else:
        #messagebox.showerror("Deletion","Contact has not been deleted")

def Edit_Contact():
    index = Contacts_list.curselection()
    # Delete the selected item
    Contacts_list.delete(index)
    
    # Get the new name and phone number
    name = edit_entry_1.get()
    phonenumber = edit_entry_2.get()

    # Create the new contact string
    contact_info = f'{name} : {phonenumber}'

    # Insert the updated contact at the same index
    Contacts_list.insert(index, contact_info)

def Edit():
    window = tk.Toplevel()

    window.geometry("270x357")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 357,
        width = 270,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        270.0,
        55.0,
        fill="#7B4040",
        outline="")

    canvas.create_text(
        11.0,
        0.0,
        anchor="nw",
        text="EDIT CONTACT",
        fill="#C9D3A3",
        font=("Anybody Regular", 20 * -1)
    )

    canvas.create_text(
        103.0,
        82.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("AnybodyItalic Medium", 16 * -1)
    )

    canvas.create_text(
        66.0,
        185.0,
        anchor="nw",
        text="Phonenumber",
        fill="#000000",
        font=("AnybodyItalic Medium", 16 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        130.5,
        133.5,
        image=entry_image_1
    )
    global edit_entry_1
    edit_entry_1 = Entry(canvas,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    edit_entry_1.place(
        x=16.0,
        y=121.0,
        width=229.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        130.5,
        236.5,
        image=entry_image_2
    )
    global edit_entry_2
    edit_entry_2 = Entry(canvas,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    edit_entry_2.place(
        x=16.0,
        y=224.0,
        width=229.0,
        height=23.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("ApplyButton.png"))
    button_1 = Button(canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Edit_Contact,
        relief="flat"
    )
    button_1.place(
        x=85.0,
        y=288.0,
        width=90.0,
        height=45.0
    )
    window.resizable(False, False)
    window.mainloop()



###################ADD CONTACT WINDOW###############

def Insert():
    Add_win = tk.Toplevel()
    Add_win.title("ADD CONTACT")

    Add_win.geometry("270x357")
    Add_win.configure(bg = "#FFFFFF")


    canvas = Canvas(Add_win,bg = "#FFFFFF", height = 357, width = 270,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0.0,0.0,270.0,55.0,fill="#7B4040",outline="")

    canvas.create_text(11.0,0.0,anchor="nw",text="ADD CONTACT",fill="#C9D3A3",font=("Anybody Regular", 20 * -1)
    )

    canvas.create_text(10.0,101.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("AnybodyItalic Medium", 16 * -1)
    )

    canvas.create_text(
        10.0,
        182.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("AnybodyItalic Medium", 16 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        125.5,
        138.5,
        image=entry_image_1
    )
    global entry_1
    entry_1 = Entry(canvas,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=11.0,
        y=126.0,
        width=229.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        125.5,
        219.5,
        image=entry_image_2
    )
    global entry_2
    entry_2 = Entry(canvas,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=11.0,
        y=207.0,
        width=229.0,
        height=23.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("ApplyButton.png"))
    button_1 = Button(canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=ApplyButtonInsert,
        relief="flat"
    )
    button_1.place(
        x=90.0,
        y=288.0,
        width=90.0,
        height=45.0
    )
    Add_win.resizable(False, False)
    Add_win.mainloop()


###CONTACT WINDOW###

window = Tk()

window.geometry("575x377")
window.configure(bg = "#FFFFFF")
window.title('Contacts')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 377,
    width = 575,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    575.0,
    68.0,
    fill="#3C4D27",
    outline="")

canvas.create_text(
    69.0,
    20.0,
    anchor="nw",
    text="Contacts",
    fill="#180847",
    font=("HappyMonkey Regular", 24 * -1)
)

Contacts_list = Listbox(bg= "lemon chiffon", height= 13, width= 65,justify="center",
                        selectbackground="dark goldenrod", relief="groove")
Contacts_list.place(x=90,y=100)
#canvas.create_rectangle(9.0,88.0,561.0,308.0,fill="#D9D9D9",outline="")

#item = canvas.create_text(280.0,120.0,anchor="n",text="Empty List",fill="#180847",font=("Arial", 18))

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Delete_Contact,
    relief="flat"
)
button_1.place(
    x=15.0,
    y=328.0,
    width=96.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Edit,
    relief="flat"
)
button_2.place(
    x=238.0,
    y=328.0,
    width=95.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Insert,### THIS FUNCTION GOES FROM CONTACT WINDOW TO ADD WINDOW ###
    relief="flat"
)
button_3.place(
    x=461.0,
    y=328.0,
    width=95.0,
    height=40.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    34.0,
    34.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()



