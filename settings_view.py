import tkinter as tk

from item_services import *

def open_new_window():

    new_window = tk.Tk()
    new_window.title('Settings')
    new_window.geometry('1000x700')
    new_window.resizable(False,False)
    new_window.focus_force()

    cancel_button = tk.Button(new_window, text='Cancel', command=new_window.destroy, width=20, height=5)
    cancel_button.place(x=840,y=610)
    item_services(new_window)
    item_buttons(new_window)
    new_window.mainloop()


def item_services(new_window):
    item_label = tk.Label(new_window, text='Items', font=('Helvetica',16))
    item_label.place(x=20,y=20)

def item_buttons(new_window):
    item_button_add = tk.Button(new_window, text='Add Items', command=add_item, width=20, height=5)
    item_button_add.place(x=20, y=50)
