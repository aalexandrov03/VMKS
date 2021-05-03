from tkinter import *
from tkinter import ttk, messagebox, Text
from order import *
from serial import *

root = Tk()
root.title("Pharmacy Machine")

app_width = 1020
app_height = 470

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

TextBox = Text(root, state="disabled", width=110, height=20, font=60)
TextBox.grid(row=1, column=1, columnspan=5, padx=10)

options = MedicineOptions()
medicines = MedicineList()
dev = DeviceList()

medicines_box = ttk.Combobox(root, width=30, font=40, state="readonly", value=options.get_medicine_options)
medicines_box.current(0)
medicines_box.grid(row=0, column=1)

quantities_box = ttk.Combobox(root, width=30, font=35, state="readonly", value=options.get_quantity_options)
quantities_box.current(0)
quantities_box.grid(row=0, column=2)


def add():
    medicine_val = medicines_box.get()
    quantity_val = quantities_box.get()

    if medicine_val != "Choose medicine:" and quantity_val != "Choose number:":
        medicines.inc_size()
        for i in range(0, int(quantity_val)):
            medicines.add(MedicineList.encode(medicine_val, options.get_medicine_options))

        TextBox.configure(state='normal')
        TextBox.insert(END, medicine_val + " x " + quantity_val + "\n")
        TextBox.configure(state='disabled')


def undo():  # To be implemented
    if len(medicines.get_list) > 0:
        TextBox.configure(state='normal')
        TextBox.delete(float(medicines.get_size), END)
        TextBox.configure(state='disabled')
        medicines.dec_size()


def clear():
    if len(medicines.get_list) > 0:
        TextBox.configure(state='normal')
        TextBox.delete(1.0, END)
        TextBox.configure(state='disabled')
        medicines.clear()


def finish():
    if dev.is_saved() != 1:
        messagebox.showerror("Error!", "Select a device first!")

    elif len(medicines.get_list) == 0:
        print(medicines.get_list)
        messagebox.showerror("Error!", "You cannot finish an empty order!")

    else:
        medicines.add('s')
        Serial.out(medicines.get_list, dev.get_list)
        messagebox.showinfo("Finished!", "Your order will be completed soon!")
        medicines.clear()
        clear()


def save(window, device, baudrate):
    dev.save(device, baudrate)
    messagebox.showinfo("Info!", "Saved!")
    window.destroy()


def select_device():
    device = Toplevel()
    width = device.winfo_screenwidth()
    height = device.winfo_screenheight()
    _x = (width / 2) - 335
    _y = (height / 2) - 100
    device.geometry(f'{670}x{200}+{int(_x)}+{int(_y)}')

    label_device = Label(device, text="Enter device:", font=60)
    input_device = Entry(device, font=60)
    label_device.grid(row=1, column=1, pady=10)
    input_device.grid(row=1, column=2, pady=20)

    label_baudrate = Label(device, text="Enter baudrate:", font=40)
    input_baudrate = Entry(device, font=40)
    label_baudrate.grid(row=2, column=1, pady=10)
    input_baudrate.grid(row=2, column=2, pady=20)

    button_save = Button(device, text="Save", width=10, font=40, command=lambda: save(device, input_device.get(),
                                                                                      input_baudrate.get()))
    button_save.grid(row=3, column=3, padx=30)

    button_cancel = Button(device, text="Cancel", width=10, font=40, command=device.destroy)
    button_cancel.grid(row=3, column=0, padx=10)

    device.transient(root)
    device.grab_set()
    root.wait_window(device)


button_add = Button(root, width=15, text="Add", font=30, command=add)
button_add.grid(row=0, column=4, pady=10)

button_undo = Button(root, width=15, text="Undo", font=30, command=undo)
button_undo.grid(row=0, column=5, pady=10)

button_clear = Button(root, width=15, text="Clear", font=40, command=clear)
button_clear.grid(row=2, column=1, pady=10)

button_device = Button(root, width=15, text="Select device", font=40, command=select_device)
button_device.grid(row=2, column=4, pady=10)

button_finish = Button(root, width=15, text="Finish", font=40, command=finish)
button_finish.grid(row=2, column=5, pady=10)

root.mainloop()
