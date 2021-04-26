from tkinter import *
from tkinter import ttk, messagebox, Text
import subprocess

root = Tk()
root.title("Pharmacy Machine")


app_width = 1125
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

global device
global baudrate

global index
index = 0.0

global List
List = ["sudo", "-S", "./a.out"]
# List.append("sudo", "./a.out")

global saved
saved = 0

TextBox = Text(root, state="disabled", width=110, height=20, font=60)
TextBox.grid(row=1, column=1, columnspan=5, padx=10)

def setupList():
    global saved
    global device
    global baudrate
    global List
    saved = 1
    List = ["sudo", "-S", "./a.out", str(device), str(baudrate)]


def add():
    global saved
    if saved:
        if Combo1.get() != "Choose medicine:" and Combo2.get() != "Choose number:":
            global List
            global index
            global number
            index += 1.0
            TextBox.configure(state='normal')
            TextBox.insert(float(index), str(Combo1.get()) + " x" + str(Combo2.get()) + ',' + '\n')
            TextBox.configure(state='disabled')
            number = int(Combo2.get())
            for x in range(0, number):
                if Combo1.get() == "Alergozan":
                    List.append("a")
                elif Combo1.get() == "Analgin":
                    List.append("b")
                elif Combo1.get() == "Dicinon":
                    List.append("c")
                elif Combo1.get() == "Espumizan":
                    List.append("d")
                elif Combo1.get() == "Elaksa piko":
                    List.append("e")
                elif Combo1.get() == "Imodium":
                    List.append("f")
                elif Combo1.get() == "Nurofen":
                    List.append("g")
                elif Combo1.get() == "Panadol":
                    List.append("h")
                elif Combo1.get() == "ParacetaMax":
                    List.append("i")
                elif Combo1.get() == "Paracetamol":
                    List.append("j")
                elif Combo1.get() == "Reparil":
                    List.append("k")
                else:
                    List.append("l")
                x += 1
    else:
        messagebox.showerror("Error!", "Select device first!")

def undo():
    global List
    global index
    global number
    if index != 0.0:
        TextBox.configure(state='normal')
        TextBox.delete(float(index), END)
        TextBox.insert(float(index), '\n')
        TextBox.configure(state='disabled')
        listlen = len(List)
        for x in range(0, number):
            listlen -= 1
            List.pop(listlen)
            x += 1
        index -= 1.0


def clear():
    global index
    index = 0.0
    TextBox.configure(state='normal')
    TextBox.delete(1.0, END)
    TextBox.configure(state='disabled')
    List.clear()
    setupList()


def SelectDevice():
    global saved
    global List
    def destroyDevice():
        device.destroy()

    def save(dev, baud):
        global device
        global baudrate
        global List
        global saved
        if dev and baud:
            device = dev
            baudrate = baud
            saved = 1
            List.append(str(dev))
            List.append(str(baud))
            messagebox.showinfo("Saved!", "Saved!")
            destroyDevice()

        else:
            messagebox.showerror("Error", "You cant save empty fileds!")

    device = Toplevel()
    app_width = 670
    app_height = 200

    screen_width = device.winfo_screenwidth()
    screen_height = device.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)


    device.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    button_cancel = Button(device, text="Cancel", width=10, font=40, command=destroyDevice)
    button_cancel.grid(row=3, column=0, padx=10)


    LabelDevice = Label(device, text="Enter device:", font=60)
    InputDevice = Entry(device, font=60)


    LabelDevice.grid(row=1, column=1, pady=10)
    InputDevice.grid(row=1, column=2, pady=20)


    LabelBaudrate = Label(device, text="Enter baudrate:", font=40)
    InputBaudrate = Entry(device, font=40)


    LabelBaudrate.grid(row=2, column=1, pady=10)
    InputBaudrate.grid(row=2, column=2, pady=20)


    button_save = Button(device, text="Save", width=10, font=40, command=lambda: save(InputDevice.get(), InputBaudrate.get()))
    button_save.grid(row=3, column=3, padx=30)

    device.transient(root)
    device.grab_set()
    root.wait_window(device)


def finish():
    global saved
    if saved:
        if len(List) < 6:
            messagebox.showerror("Error", "You cant finish empty order!")
        else:
            List.append("s")
            saved = 0
            print(List)
            subprocess.run(List)
            messagebox.showinfo("Finished!", "Your order will be completed very soon!")
            clear()
    else:
        messagebox.showerror("Error!", "Select device first!")


options1 = [
    "Choose medicine:",
    "Alergozan",
    "Analgin",
    "Dicinon",
    "Espumizan",
    "Elaksa piko",
    "Imodium",
    "Nurofen",
    "Panadol",
    "ParacetaMax",
    "Paracetamol",
    "Reparil gel",
    "Remantadin",
]

options2 = [
    "Choose number:",
    "1",
    "2",
    "3",
]

Combo1 = ttk.Combobox(root, width=30, font=40, state="readonly", value=options1)
Combo1.current(0)
Combo1.grid(row=0, column=1)

Combo2 = ttk.Combobox(root, width=30, font=35, state="readonly", value=options2)
Combo2.current(0)
Combo2.grid(row=0, column=2)

button_add = Button(root, width=15, text="Add to List", font=30, command=add)
button_undo = Button(root, width=15, text="Undo", font=30, command=undo)

button_add.grid(row=0, column=4, pady=10)
button_undo.grid(row=0, column=5, pady=10)

button_clear = Button(root, width=15, text="Clear the list", font=40, command=clear)
button_device = Button(root, width=15, text="Select device", font=40, command=SelectDevice)
button_finish = Button(root, width=15, text="Finish", font=40, command=finish)

button_clear.grid(row=2, column=1, pady=10)
button_device.grid(row=2, column=4, pady=10)
button_finish.grid(row=2, column=5, pady=10)

root.mainloop()
