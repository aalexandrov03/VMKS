from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Pharmacy Machine")
root.geometry("825x430")

global index
index = 0.0

global List
List = []

TextBox = Text(root, state="disabled", width=100, height=20)
TextBox.grid(row=1, column=1, columnspan=5, padx=10)


def add():
    if Combo1.get() != "Choose option:" and Combo2.get() != "Choose option:":
        global List
        global index
        global counter
        index += 1.0
        TextBox.configure(state='normal')
        TextBox.insert(float(index), str(Combo1.get()) + " x" + str(Combo2.get()) + ',' + '\n')
        TextBox.configure(state='disabled')
        counter = int(Combo2.get())
        for x in range(0, counter):
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
    global counter
    if index != 0.0:
        TextBox.configure(state='normal')
        TextBox.delete(float(index), END)
        TextBox.insert(float(index), '\n')
        TextBox.configure(state='disabled')
        l = len(List)
        for x in range(0, counter):
            l -= 1
            List.pop(l)
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
    "Choose option:",
    "Analgin",
    "Elaksa piko",
    "Espumizan",
    "Nurofen",
    "Reparil gel",

]

options2 = [
    "Choose option:",
    "1",
    "2",
    "3",
]

Combo1 = ttk.Combobox(root, font=20, state="readonly", value=options1)
Combo1.current(0)
Combo1.grid(row=0, column=1)

Combo2 = ttk.Combobox(root, font=20, state="readonly", value=options2)
Combo2.current(0)
Combo2.grid(row=0, column=2)

button_add = Button(root, text="Add to List", font=20, command=add)
button_undo = Button(root, text="Undo", font=20, command=undo)

button_add.grid(row=0, column=4, pady=10)
button_undo.grid(row=0, column=5, pady=10)

button_clear = Button(root, text="Clear the list", font=20, command=clear)
button_finish = Button(root, text="Finish", font=20, command=finish)

button_clear.grid(row=2, column=1, pady=10)
button_finish.grid(row=2, column=5, pady=10)

root.mainloop()
