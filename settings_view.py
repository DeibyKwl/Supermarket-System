import tkinter as tk

from basket_services import *
import setting_services as setting
from json_script import staff_json



all_staff = staff_json.retrieve_all_staffs()

# Make sure it is always focused on the entry for the barcode
def set_focus(event, entry_barcode):
    # Check if the focus should be set to entry_barcode
    if event.widget != entry_barcode:
        entry_barcode.focus_set()

# Create the security window to check if user is a staff member
def security_window():

    security_window = tk.Tk()
    security_window.title('Checking staff')
    security_window.geometry('400x400')
    security_window.configure(background='red')
    security_window.resizable(False,False)
    security_window.focus_force()

    label = tk.Label(security_window, text='Checking for staff...', font=('Helvetica', 20))
    label.place(x=80, y=150)

    cancel_button = tk.Button(security_window, text='Cancel', command=security_window.destroy, width=20, height=5)
    cancel_button.place(x=130,y=310)

    # Search the item by barcode 
    entry_barcode = tk.Entry(security_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable

    entry_barcode.bind('<Return>', lambda event: setting_window(entry_barcode, security_window))

    security_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    security_window.mainloop()

# Open setting window if user is a staff member, deny otherwise
def setting_window(entry_barcode, security_window):

    staff_json.file_checker()
    all_staff = staff_json.retrieve_all_staffs()
    barcode = str(entry_barcode.get())
    security_window.destroy()
    if barcode in all_staff:
        setting_window = tk.Tk()
        setting_window.title('Settings')
        setting_window.geometry('1000x700')
        setting_window.resizable(False,False)
        setting_window.focus_force()

        cancel_button = tk.Button(setting_window, text='Cancel', command=setting_window.destroy, width=20, height=5)
        cancel_button.place(x=840,y=610)
        item_label(setting_window)
        staff_label(setting_window)
        credit_label(setting_window)
        item_buttons(setting_window)
        staff_buttons(setting_window)
        credit_buttons(setting_window)

        setting_window.mainloop()

    elif barcode not in all_staff:
        not_staff_window = tk.Tk()
        not_staff_window.title('')
        not_staff_window.geometry('300x300')
        not_staff_window.configure(background='yellow')
        not_staff_window.resizable(False, False)
        not_staff_window.focus_force()

        label = tk.Label(not_staff_window, text='Sorry, staff not in the system', font=('Helvetica', 16))
        label.place(x=10,y=30)

        ok_button = tk.Button(not_staff_window, text='OK', width=20, height=5)
        ok_button.config(command=not_staff_window.destroy)
        ok_button.place(x=80,y=100)

        not_staff_window.mainloop()



def item_label(setting_window):
    item_label = tk.Label(setting_window, text='Items', font=('Helvetica',16))
    item_label.place(x=110,y=20)

def staff_label(setting_window):
     staff_label = tk.Label(setting_window, text='Staff', font=('Helvetica',16))
     staff_label.place(x=460,y=20)

def credit_label(setting_window):
     credit_label = tk.Label(setting_window, text='Credit', font=('Helvetica',16))
     credit_label.place(x=810,y=20)

def item_buttons(setting_window):
    item_button_add = tk.Button(setting_window, text='Add Item', command=setting.add_item, width=18, height=4)
    item_button_add.place(x=70, y=100)

    item_button_remove = tk.Button(setting_window, text='Remove Item', command=setting.remove_item, width=18, height=4)
    item_button_remove.place(x=70,y=190)

    item_button_update = tk.Button(setting_window, text='Update Item', command=setting.update_item, width=18, height=4)
    item_button_update.place(x=70,y=280)

    item_button_view = tk.Button(setting_window, text='View Item', command=setting.view_item, width=18, height=4)
    item_button_view.place(x=70,y=370)

    item_button_viewall = tk.Button(setting_window, text='View All Items', command=setting.view_all_items, width=18, height=4)
    item_button_viewall.place(x=70,y=460)

def staff_buttons(setting_window):
    staff_button_add = tk.Button(setting_window, text='Add Staff', command=setting.add_staff, width=18, height=4)
    staff_button_add.place(x=415,y=100)

    staff_button_remove = tk.Button(setting_window, text='Remove Staff', command=setting.remove_staff, width=18, height=4)
    staff_button_remove.place(x=415,y=190)

    staff_button_update = tk.Button(setting_window, text='Update Staff', command=setting.update_staff, width=18, height=4)
    staff_button_update.place(x=415,y=280)

    staff_button_view = tk.Button(setting_window, text='View Staff', command=setting.view_staff, width=18, height=4)
    staff_button_view.place(x=415,y=370)

    staff_button_viewall = tk.Button(setting_window, text='View All Staffs', command=setting.view_all_staffs, width=18, height=4)
    staff_button_viewall.place(x=415,y=460)

def credit_buttons(setting_window):
    credit_button_add = tk.Button(setting_window, text='Add Credit Card', command=setting.add_card, width=18, height=4)
    credit_button_add.place(x=770,y=100)

    credit_button_remove = tk.Button(setting_window, text='Remove Credit Card', command=setting.remove_credit_card, width=18, height=4)
    credit_button_remove.place(x=770,y=190)

    credit_button_update = tk.Button(setting_window, text='Update Credit Card', command=setting.update_card, width=18, height=4)
    credit_button_update.place(x=770,y=280)

    credit_button_view = tk.Button(setting_window, text='View Credit Card', command=setting.view_card, width=18, height=4)
    credit_button_view.place(x=770,y=370)

    credit_button_viewall = tk.Button(setting_window, text='View All Credit Cards', command=setting.view_all_cards, width=18, height=4)
    credit_button_viewall.place(x=770,y=460)
