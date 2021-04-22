from tkinter import *
from tkinter import ttk, messagebox, Text

root = Tk()
root.title("Pharmacy Machine")

app_width = 1020
app_height = 470

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

global index
index = 0.0

global List
List = []

TextBox = Text(root, state="disabled", width=110, height=20, font=60)
TextBox.grid(row=1, column=1, columnspan=5, padx=10)


def add():
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
            if Combo1.get() == "Analgin":
                List.append("a")
            elif Combo1.get() == "Elaksa piko":
                List.append("b")
            elif Combo1.get() == "Espumizan":
                List.append("c")
            elif Combo1.get() == "Nurofen":
                List.append("d")
            else:
                List.append("e")
            x += 1


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


def finish():
    List.append(0x01)
    if len(List) == 1:
        messagebox.showerror("Error", "You cant finish empty order!")
    else:
        messagebox.showinfo("Finished!", "Your order will be completed very soon!")
    clear()



options1 = [
    "Choose medicine:",
    "Analgin",
    "Elaksa piko",
    "Espumizan",
    "Nurofen",
    "Reparil gel",

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
button_finish = Button(root, width=15, text="Finish", font=40, command=finish)

button_clear.grid(row=2, column=1, pady=10)
button_finish.grid(row=2, column=5, pady=10)

root.mainloop()
