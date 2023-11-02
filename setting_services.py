import tkinter as tk
from json_script import item_json
from json_script import staff_json
from json_script import credit_json

# Make sure it is always focused on the entry for the barcode
def set_focus(event, entry_barcode):
    # Check if the focus should be set to entry_barcode
    if event.widget != entry_barcode:
        entry_barcode.focus_set()


def add_item():

    scan_item_window = tk.Tk()
    scan_item_window.title('Adding item to the system')
    scan_item_window.geometry('400x400')
    scan_item_window.resizable(False, False)
    scan_item_window.focus_force()

    
    label = tk.Label(scan_item_window, text='Scan Item to add...', font=('Helvetica', 20))
    label.place(x=65, y=150)

    entry_barcode = tk.Entry(scan_item_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: add_item_checker(entry_barcode))

    quit_button = tk.Button(scan_item_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_item_window.destroy)
    quit_button.place(x=230,y=300)

    scan_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_item_window.mainloop()

# Here we would determine if adding the item to the system. (TODO: Change structure)
def add_item_checker(entry_barcode):
    item_json.file_checker()
    all_items = item_json.retrieve_all_items()
    barcode = str(entry_barcode.get())
    if barcode not in all_items:
        add_item_window = tk.Tk()
        add_item_window.title('Adding item to the system')
        add_item_window.geometry('560x500')
        add_item_window.resizable(False, False)
        add_item_window.focus_force()

        name_label = tk.Label(add_item_window, text='Product name', font=('Helvetica', 15))
        name_label.place(x=20,y=40)
        entry_name = tk.Entry(add_item_window, width=30, font=('Helvetica', 15))
        entry_name.place(x=200,y=40)

        price_label = tk.Label(add_item_window, text='Price of product', font=('Helvetica', 15))
        price_label.place(x=20,y=120)
        entry_price = tk.Entry(add_item_window, width=30, font=('Helvetica', 15))
        entry_price.place(x=200,y=120)

        section_label = tk.Label(add_item_window, text='Section', font=('Helvetica', 15))
        section_label.place(x=20,y=200)
        entry_section = tk.Entry(add_item_window, width=30, font=('Helvetica', 15))
        entry_section.place(x=200,y=200)

        quantity_label = tk.Label(add_item_window, text='Quantity', font=('Helvetica', 15))
        quantity_label.place(x=20,y=280)
        entry_quantity = tk.Entry(add_item_window, width=30, font=('Helvetica', 15))
        entry_quantity.place(x=200,y=280)

        save_button = tk.Button(add_item_window, text='Save', width=20, height=5)
        save_button.config(command=lambda: add_item_to_json(barcode, add_item_window, entry_name.get(), entry_price.get(), entry_section.get(), entry_quantity.get()))
        save_button.place(x=400,y=400)

        quit_button = tk.Button(add_item_window, text='Quit', width=20, height=5)
        quit_button.config(command=add_item_window.destroy)
        quit_button.place(x=10,y=400)

        entry_barcode.delete(0, tk.END)
        add_item_window.mainloop()

    elif barcode in all_items:
        not_item_window = tk.Tk()
        not_item_window.title('')
        not_item_window.geometry('300x300')
        not_item_window.configure(background='yellow')
        not_item_window.resizable(False, False)
        not_item_window.focus_force()

        label = tk.Label(not_item_window, text='Item already on the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_item_window, text='OK', width=20, height=5)
        ok_button.config(command=not_item_window.destroy)
        ok_button.place(x=80,y=100)

        not_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_item_window.mainloop()


def add_item_to_json(barcode, add_item_window, entry_name, entry_price, entry_section, entry_quantity):

    name = entry_name
    # TODO: make sure there is no negative number
    price = round(float(entry_price), 2)
    section = str(entry_section)
    # TODO: make sure there is no negative number
    quantity = int(entry_quantity)
    item_json.add_item(barcode, name, price, section, quantity)
    add_item_window.destroy()



def add_staff():

    scan_staff_window = tk.Tk()
    scan_staff_window.title('Adding staff to the system')
    scan_staff_window.geometry('400x400')
    scan_staff_window.resizable(False, False)
    scan_staff_window.focus_force()

    
    label = tk.Label(scan_staff_window, text='Scan staff code to add...', font=('Helvetica', 20))
    label.place(x=50, y=150)

    entry_barcode = tk.Entry(scan_staff_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: add_staff_checker(entry_barcode))

    quit_button = tk.Button(scan_staff_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_staff_window.destroy)
    quit_button.place(x=230,y=300)

    scan_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_staff_window.mainloop()

# Here we would determine if adding the item to the system. (TODO: Change structure)
def add_staff_checker(entry_barcode):
    staff_json.file_checker()
    all_staffs = staff_json.retrieve_all_staffs()
    barcode = str(entry_barcode.get())
    if barcode not in all_staffs:
        add_staff_window = tk.Tk()
        add_staff_window.title('Adding staff to the system')
        add_staff_window.geometry('560x250')
        add_staff_window.resizable(False, False)
        add_staff_window.focus_force()

        name_label = tk.Label(add_staff_window, text='Staff name', font=('Helvetica', 15))
        name_label.place(x=20,y=40)
        entry_name = tk.Entry(add_staff_window, width=30, font=('Helvetica', 15))
        entry_name.place(x=200,y=40)

        save_button = tk.Button(add_staff_window, text='Save', width=20, height=5)
        save_button.config(command=lambda: add_staff_to_json(barcode, add_staff_window, entry_name.get()))
        save_button.place(x=400,y=150)

        quit_button = tk.Button(add_staff_window, text='Quit', width=20, height=5)
        quit_button.config(command=add_staff_window.destroy)
        quit_button.place(x=10,y=150)

        entry_barcode.delete(0, tk.END)
        add_staff_window.mainloop()

    elif barcode in all_staffs:
        not_staff_window = tk.Tk()
        not_staff_window.title('')
        not_staff_window.geometry('300x300')
        not_staff_window.configure(background='yellow')
        not_staff_window.resizable(False, False)
        not_staff_window.focus_force()

        label = tk.Label(not_staff_window, text='Staff already on the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_staff_window, text='OK', width=20, height=5)
        ok_button.config(command=not_staff_window.destroy)
        ok_button.place(x=80,y=100)

        not_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_staff_window.mainloop()


def add_staff_to_json(barcode, add_staff_window, entry_name):

    name = entry_name
    staff_json.add_staff(barcode, name)
    add_staff_window.destroy()






def add_card():

    scan_card_window = tk.Tk()
    scan_card_window.title('Adding card to the system')
    scan_card_window.geometry('400x400')
    scan_card_window.resizable(False, False)
    scan_card_window.focus_force()

    
    label = tk.Label(scan_card_window, text='Scan card code to add...', font=('Helvetica', 20))
    label.place(x=50, y=150)

    entry_barcode = tk.Entry(scan_card_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: add_card_checker(entry_barcode))

    quit_button = tk.Button(scan_card_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_card_window.destroy)
    quit_button.place(x=230,y=300)

    scan_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_card_window.mainloop()

# Here we would determine if adding the item to the system. (TODO: Change structure)
def add_card_checker(entry_barcode):
    credit_json.file_checker()
    all_cards = credit_json.retrieve_all_cards()
    barcode = str(entry_barcode.get())
    if barcode not in all_cards:
        add_card_window = tk.Tk()
        add_card_window.title('Adding card to the system')
        add_card_window.geometry('560x330')
        add_card_window.resizable(False, False)
        add_card_window.focus_force()

        name_label = tk.Label(add_card_window, text='Name', font=('Helvetica', 15))
        name_label.place(x=20,y=40)
        entry_name = tk.Entry(add_card_window, width=30, font=('Helvetica', 15))
        entry_name.place(x=200,y=40)

        credit_label = tk.Label(add_card_window, text='Initial credit', font=('Helvetica', 15))
        credit_label.place(x=20,y=120)
        entry_credit = tk.Entry(add_card_window, width=30, font=('Helvetica', 15))
        entry_credit.place(x=200,y=120)

        save_button = tk.Button(add_card_window, text='Save', width=20, height=5)
        save_button.config(command=lambda: add_card_to_json(barcode, add_card_window, entry_name.get(), entry_credit.get()))
        save_button.place(x=400,y=230)

        quit_button = tk.Button(add_card_window, text='Quit', width=20, height=5)
        quit_button.config(command=add_card_window.destroy)
        quit_button.place(x=10,y=230)

        entry_barcode.delete(0, tk.END)
        add_card_window.mainloop()

    elif barcode in all_cards:
        not_staff_window = tk.Tk()
        not_staff_window.title('')
        not_staff_window.geometry('300x300')
        not_staff_window.configure(background='yellow')
        not_staff_window.resizable(False, False)
        not_staff_window.focus_force()

        label = tk.Label(not_staff_window, text='Card already on the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_staff_window, text='OK', width=20, height=5)
        ok_button.config(command=not_staff_window.destroy)
        ok_button.place(x=80,y=100)

        not_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_staff_window.mainloop()


def add_card_to_json(barcode, add_card_window, entry_name, entry_credit):

    name = entry_name
    credit = int(entry_credit)
    credit_json.add_card(barcode, name, credit)
    add_card_window.destroy()




def remove_item():

    remove_item_window = tk.Tk()
    remove_item_window.title('Remove item from system')
    remove_item_window.geometry('400x400')
    remove_item_window.resizable(False, False)
    remove_item_window.focus_force()

    label = tk.Label(remove_item_window, text='Scan Item to remove...', font=('Helvetica', 20))
    label.place(x=65, y=150)

    quit_button = tk.Button(remove_item_window, text='Quit', width=20, height=5)
    quit_button.config(command=remove_item_window.destroy)
    quit_button.place(x=230,y=300)

    entry_barcode = tk.Entry(remove_item_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: remove_item_checker(entry_barcode))

    remove_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    remove_item_window.mainloop()

def remove_item_checker(entry_barcode):
    item_json.file_checker()
    all_items = item_json.retrieve_all_items()
    barcode = str(entry_barcode.get())
    if barcode in all_items:
        confirm_window = tk.Tk()
        confirm_window.title('')
        confirm_window.geometry('300x300')
        confirm_window.resizable(False, False)
        confirm_window.focus_force()

        label = tk.Label(confirm_window, text='Are you sure?', font=('Helvetica', 16))
        label.place(x=80,y=30)  

        yes_button = tk.Button(confirm_window, text='Yes', width=15, height=4, bg='Green', fg='white', font=('Helvetica', 10))
        yes_button.config(command=lambda:[item_json.remove_item(barcode), confirm_window.destroy()])
        yes_button.place(x=18,y=100)

        no_button = tk.Button(confirm_window, text='No', width=15, height=4, bg='Red', fg='white', font=('Helvetica', 10))
        no_button.config(command=confirm_window.destroy)
        no_button.place(x=160,y=100)

        entry_barcode.delete(0, tk.END)
        confirm_window.mainloop()

    elif entry_barcode.get() not in all_items:
        not_item_window = tk.Tk()
        not_item_window.title('')
        not_item_window.geometry('300x300')
        not_item_window.configure(background='yellow')
        not_item_window.resizable(False, False)
        not_item_window.focus_force()

        label = tk.Label(not_item_window, text='Sorry, Item not in the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_item_window, text='OK', width=20, height=5)
        ok_button.config(command=not_item_window.destroy)
        ok_button.place(x=80,y=100)

        not_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_item_window.mainloop()


def remove_staff():

    remove_staff_window = tk.Tk()
    remove_staff_window.title('Remove staff from system')
    remove_staff_window.geometry('400x400')
    remove_staff_window.resizable(False, False)
    remove_staff_window.focus_force()

    label = tk.Label(remove_staff_window, text='Scan staff code to remove...', font=('Helvetica', 20))
    label.place(x=40, y=150)

    quit_button = tk.Button(remove_staff_window, text='Quit', width=20, height=5)
    quit_button.config(command=remove_staff_window.destroy)
    quit_button.place(x=230,y=300)

    entry_barcode = tk.Entry(remove_staff_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: remove_staff_checker(entry_barcode))

    remove_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

    remove_staff_window.mainloop()

def remove_staff_checker(entry_barcode):
    staff_json.file_checker()
    all_staffs = staff_json.retrieve_all_staffs()
    barcode = str(entry_barcode.get())
    if barcode in all_staffs:
        confirm_window = tk.Tk()
        confirm_window.title('')
        confirm_window.geometry('300x300')
        confirm_window.resizable(False, False)
        confirm_window.focus_force()

        label = tk.Label(confirm_window, text='Are you sure?', font=('Helvetica', 16))
        label.place(x=80,y=30)  

        yes_button = tk.Button(confirm_window, text='Yes', width=15, height=4, bg='Green', fg='white', font=('Helvetica', 10))
        yes_button.config(command=lambda:[staff_json.remove_staff(barcode), confirm_window.destroy()])
        yes_button.place(x=18,y=100)

        no_button = tk.Button(confirm_window, text='No', width=15, height=4, bg='Red', fg='white', font=('Helvetica', 10))
        no_button.config(command=confirm_window.destroy)
        no_button.place(x=160,y=100)

        entry_barcode.delete(0, tk.END)
        confirm_window.mainloop()

    elif entry_barcode.get() not in all_staffs:
        not_staff_window = tk.Tk()
        not_staff_window.title('')
        not_staff_window.geometry('300x300')
        not_staff_window.configure(background='yellow')
        not_staff_window.resizable(False, False)
        not_staff_window.focus_force()

        label = tk.Label(not_staff_window, text='Sorry, staff not in the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_staff_window, text='OK', width=20, height=5)
        ok_button.config(command=not_staff_window.destroy)
        ok_button.place(x=80,y=100)

        not_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_staff_window.mainloop()


def remove_credit_card():

    remove_credit_card_window = tk.Tk()
    remove_credit_card_window.title('Remove card from system')
    remove_credit_card_window.geometry('400x400')
    remove_credit_card_window.resizable(False, False)
    remove_credit_card_window.focus_force()

    label = tk.Label(remove_credit_card_window, text='Scan card code to remove...', font=('Helvetica', 20))
    label.place(x=40, y=150)

    quit_button = tk.Button(remove_credit_card_window, text='Quit', width=20, height=5)
    quit_button.config(command=remove_credit_card_window.destroy)
    quit_button.place(x=230,y=300)

    entry_barcode = tk.Entry(remove_credit_card_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: remove_card_checker(entry_barcode))

    remove_credit_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

    remove_credit_card_window.mainloop()

def remove_card_checker(entry_barcode):
    credit_json.file_checker()
    all_credit_cards = credit_json.retrieve_all_cards()
    barcode = str(entry_barcode.get())
    if barcode in all_credit_cards:
        confirm_window = tk.Tk()
        confirm_window.title('')
        confirm_window.geometry('300x300')
        confirm_window.resizable(False, False)
        confirm_window.focus_force()

        label = tk.Label(confirm_window, text='Are you sure?', font=('Helvetica', 16))
        label.place(x=80,y=30)  

        yes_button = tk.Button(confirm_window, text='Yes', width=15, height=4, bg='Green', fg='white', font=('Helvetica', 10))
        yes_button.config(command=lambda:[credit_json.remove_card(barcode), confirm_window.destroy()])
        yes_button.place(x=18,y=100)

        no_button = tk.Button(confirm_window, text='No', width=15, height=4, bg='Red', fg='white', font=('Helvetica', 10))
        no_button.config(command=confirm_window.destroy)
        no_button.place(x=160,y=100)

        entry_barcode.delete(0, tk.END)
        confirm_window.mainloop()

    elif entry_barcode.get() not in all_credit_cards:
        not_card_window = tk.Tk()
        not_card_window.title('')
        not_card_window.geometry('300x300')
        not_card_window.configure(background='yellow')
        not_card_window.resizable(False, False)
        not_card_window.focus_force()

        label = tk.Label(not_card_window, text='Sorry, card not in the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_card_window, text='OK', width=20, height=5)
        ok_button.config(command=not_card_window.destroy)
        ok_button.place(x=80,y=100)

        not_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_card_window.mainloop()




def update_item():

    scan_item_window = tk.Tk()
    scan_item_window.title('Updating item to the system')
    scan_item_window.geometry('400x400')
    scan_item_window.resizable(False, False)
    scan_item_window.focus_force()

    
    label = tk.Label(scan_item_window, text='Scan Item to update...', font=('Helvetica', 20))
    label.place(x=65, y=150)

    entry_barcode = tk.Entry(scan_item_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: update_item_checker(entry_barcode))

    quit_button = tk.Button(scan_item_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_item_window.destroy)
    quit_button.place(x=230,y=300)

    scan_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_item_window.mainloop()

# Here we would determine if adding the item to the system. (TODO: Change structure)
def update_item_checker(entry_barcode):
    item_json.file_checker()
    all_items = item_json.retrieve_all_items()
    barcode = str(entry_barcode.get())
    if barcode in all_items:

        item = item_json.retrieve_item(barcode)

        update_item_window = tk.Tk()
        update_item_window.title('Updating item to the system')
        update_item_window.geometry('560x500')
        update_item_window.resizable(False, False)
        update_item_window.focus_force()

        name_label = tk.Label(update_item_window, text='Product name', font=('Helvetica', 15))
        name_label.place(x=20,y=40)
        entry_name = tk.Entry(update_item_window, width=30, font=('Helvetica', 15))
        entry_name.place(x=200,y=40)
        entry_name.insert(0, item['name'])

        price_label = tk.Label(update_item_window, text='Price of product', font=('Helvetica', 15))
        price_label.place(x=20,y=120)
        entry_price = tk.Entry(update_item_window, width=30, font=('Helvetica', 15))
        entry_price.place(x=200,y=120)
        entry_price.insert(0, item['price'])

        section_label = tk.Label(update_item_window, text='Section', font=('Helvetica', 15))
        section_label.place(x=20,y=200)
        entry_section = tk.Entry(update_item_window, width=30, font=('Helvetica', 15))
        entry_section.place(x=200,y=200)
        entry_section.insert(0, item['section'])

        quantity_label = tk.Label(update_item_window, text='Quantity', font=('Helvetica', 15))
        quantity_label.place(x=20,y=280)
        entry_quantity = tk.Entry(update_item_window, width=30, font=('Helvetica', 15))
        entry_quantity.place(x=200,y=280)
        entry_quantity.insert(0, item['quantity'])

        save_button = tk.Button(update_item_window, text='Save', width=20, height=5)
        save_button.config(command=lambda: update_item_to_json(barcode, update_item_window, entry_name.get(), entry_price.get(), entry_section.get(), entry_quantity.get()))
        save_button.place(x=400,y=400)

        quit_button = tk.Button(update_item_window, text='Quit', width=20, height=5)
        quit_button.config(command=update_item_window.destroy)
        quit_button.place(x=10,y=400)

        entry_barcode.delete(0, tk.END)
        update_item_window.mainloop()

    elif barcode not in all_items:
        not_item_window = tk.Tk()
        not_item_window.title('')
        not_item_window.geometry('300x300')
        not_item_window.configure(background='yellow')
        not_item_window.resizable(False, False)
        not_item_window.focus_force()

        label = tk.Label(not_item_window, text='Item not on the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_item_window, text='OK', width=20, height=5)
        ok_button.config(command=not_item_window.destroy)
        ok_button.place(x=80,y=100)

        not_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_item_window.mainloop()


def update_item_to_json(barcode, update_item_window, entry_name, entry_price, entry_section, entry_quantity):

    name = entry_name
    # TODO: make sure there is no negative number
    price = round(float(entry_price), 2)
    section = str(entry_section)
    # TODO: make sure there is no negative number
    quantity = int(entry_quantity)
    item_json.add_item(barcode, name, price, section, quantity)
    update_item_window.destroy()



def update_staff():

    scan_staff_window = tk.Tk()
    scan_staff_window.title('Updating staff to the system')
    scan_staff_window.geometry('400x400')
    scan_staff_window.resizable(False, False)
    scan_staff_window.focus_force()
    
    label = tk.Label(scan_staff_window, text='Scan staff code to update...', font=('Helvetica', 20))
    label.place(x=55, y=150)

    entry_barcode = tk.Entry(scan_staff_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: update_staff_checker(entry_barcode))

    quit_button = tk.Button(scan_staff_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_staff_window.destroy)
    quit_button.place(x=230,y=300)

    scan_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_staff_window.mainloop()

# Here we would determine if adding the staff to the system. (TODO: Change structure)
def update_staff_checker(entry_barcode):
    staff_json.file_checker()
    all_staffs = staff_json.retrieve_all_staffs()
    barcode = str(entry_barcode.get())
    if barcode in all_staffs:

        staff = staff_json.retrieve_staff(barcode)

        update_staff_window = tk.Tk()
        update_staff_window.title('Updating staff to the system')
        update_staff_window.geometry('560x250')
        update_staff_window.resizable(False, False)
        update_staff_window.focus_force()

        name_label = tk.Label(update_staff_window, text='Staff name', font=('Helvetica', 15))
        name_label.place(x=20,y=40)
        entry_name = tk.Entry(update_staff_window, width=30, font=('Helvetica', 15))
        entry_name.place(x=200,y=40)
        entry_name.insert(0, staff['name'])

        save_button = tk.Button(update_staff_window, text='Save', width=20, height=5)
        save_button.config(command=lambda: update_staff_to_json(barcode, update_staff_window, entry_name.get()))
        save_button.place(x=400,y=150)

        quit_button = tk.Button(update_staff_window, text='Quit', width=20, height=5)
        quit_button.config(command=update_staff_window.destroy)
        quit_button.place(x=10,y=150)

        entry_barcode.delete(0, tk.END)
        update_staff_window.mainloop()

    elif barcode not in all_staffs:
        not_staff_window = tk.Tk()
        not_staff_window.title('')
        not_staff_window.geometry('300x300')
        not_staff_window.configure(background='yellow')
        not_staff_window.resizable(False, False)
        not_staff_window.focus_force()

        label = tk.Label(not_staff_window, text='Staff not on the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_staff_window, text='OK', width=20, height=5)
        ok_button.config(command=not_staff_window.destroy)
        ok_button.place(x=80,y=100)

        not_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_staff_window.mainloop()


def update_staff_to_json(barcode, update_staff_window, entry_name):

    name = entry_name
    staff_json.add_staff(barcode, name)
    update_staff_window.destroy()



def update_card():

    scan_card_window = tk.Tk()
    scan_card_window.title('Updating card to the system')
    scan_card_window.geometry('400x400')
    scan_card_window.resizable(False, False)
    scan_card_window.focus_force()
    
    label = tk.Label(scan_card_window, text='Scan card code to update...', font=('Helvetica', 20))
    label.place(x=55, y=150)

    entry_barcode = tk.Entry(scan_card_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: update_card_checker(entry_barcode))

    quit_button = tk.Button(scan_card_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_card_window.destroy)
    quit_button.place(x=230,y=300)

    scan_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_card_window.mainloop()

# Here we would determine if adding the staff to the system. (TODO: Change structure)
def update_card_checker(entry_barcode):
    credit_json.file_checker()
    all_cards = credit_json.retrieve_all_cards()
    barcode = str(entry_barcode.get())
    if barcode in all_cards:

        card = credit_json.retrieve_card(barcode)

        update_card_window = tk.Tk()
        update_card_window.title('Updating card to the system')
        update_card_window.geometry('560x250')
        update_card_window.resizable(False, False)
        update_card_window.focus_force()

        name_label = tk.Label(update_card_window, text='Name', font=('Helvetica', 15))
        name_label.place(x=20,y=40)
        entry_name = tk.Entry(update_card_window, width=30, font=('Helvetica', 15))
        entry_name.place(x=200,y=40)
        entry_name.insert(0, card['name'])

        credit_label = tk.Label(update_card_window, text='Credit', font=('Helvetica', 15))
        credit_label.place(x=20,y=120)
        entry_credit = tk.Entry(update_card_window, width=30, font=('Helvetica', 15))
        entry_credit.place(x=200,y=120)
        entry_credit.insert(0, card['credit'])

        save_button = tk.Button(update_card_window, text='Save', width=20, height=5)
        save_button.config(command=lambda: update_card_to_json(barcode, update_card_window, entry_name.get(), entry_credit.get()))
        save_button.place(x=400,y=150)

        quit_button = tk.Button(update_card_window, text='Quit', width=20, height=5)
        quit_button.config(command=update_card_window.destroy)
        quit_button.place(x=10,y=150)

        entry_barcode.delete(0, tk.END)
        update_card_window.mainloop()

    elif barcode not in all_cards:
        not_card_window = tk.Tk()
        not_card_window.title('')
        not_card_window.geometry('300x300')
        not_card_window.configure(background='yellow')
        not_card_window.resizable(False, False)
        not_card_window.focus_force()

        label = tk.Label(not_card_window, text='Card not on the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_card_window, text='OK', width=20, height=5)
        ok_button.config(command=not_card_window.destroy)
        ok_button.place(x=80,y=100)

        not_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_card_window.mainloop()


def update_card_to_json(barcode, update_card_window, entry_name, entry_credit):

    name = entry_name
    credit = int(entry_credit)
    credit_json.add_card(barcode, name, credit)
    update_card_window.destroy()



def view_item():
    scan_item_window = tk.Tk()
    scan_item_window.title('View item in the system')
    scan_item_window.geometry('400x400')
    scan_item_window.resizable(False, False)
    scan_item_window.focus_force()

    label = tk.Label(scan_item_window, text='Scan Item to view...', font=('Helvetica', 20))
    label.place(x=55, y=150)

    entry_barcode = tk.Entry(scan_item_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: view_item_checker(entry_barcode))

    quit_button = tk.Button(scan_item_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_item_window.destroy)
    quit_button.place(x=230,y=300)

    scan_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_item_window.mainloop()

# Here we would determine if adding the item to the system. (TODO: Change structure)
def view_item_checker(entry_barcode):
    item_json.file_checker()
    all_items = item_json.retrieve_all_items()
    barcode = str(entry_barcode.get())
    if barcode in all_items:

        item = item_json.retrieve_item(barcode)

        view_item_window = tk.Tk()
        view_item_window.title('Viewing item in the system')
        view_item_window.resizable(False, False)
        view_item_window.focus_force()

        name_label = tk.Label(view_item_window, text='Product name: ' + str(item['name']), font=('Helvetica', 15))
        name_label.pack()

        price_label = tk.Label(view_item_window, text='Price of product: ' + str(item['price']), font=('Helvetica', 15))
        price_label.pack()

        section_label = tk.Label(view_item_window, text='Section: ' + str(item['section']), font=('Helvetica', 15))
        section_label.pack()

        quantity_label = tk.Label(view_item_window, text='Quantity: ' + str(item['quantity']), font=('Helvetica', 15))
        quantity_label.pack()

        quit_button = tk.Button(view_item_window, text='Quit', width=15, height=4)
        quit_button.config(command=view_item_window.destroy)
        quit_button.pack()

        entry_barcode.delete(0, tk.END)
        view_item_window.mainloop()

    elif barcode not in all_items:
        not_item_window = tk.Tk()
        not_item_window.title('')
        not_item_window.geometry('300x300')
        not_item_window.configure(background='yellow')
        not_item_window.resizable(False, False)
        not_item_window.focus_force()

        label = tk.Label(not_item_window, text='Item not in the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_item_window, text='OK', width=20, height=5)
        ok_button.config(command=not_item_window.destroy)
        ok_button.place(x=80,y=100)

        not_item_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_item_window.mainloop()



def view_staff():
    scan_staff_window = tk.Tk()
    scan_staff_window.title('View staff in the system')
    scan_staff_window.geometry('400x400')
    scan_staff_window.resizable(False, False)
    scan_staff_window.focus_force()

    label = tk.Label(scan_staff_window, text='Scan staff code to view...', font=('Helvetica', 20))
    label.place(x=55, y=150)

    entry_barcode = tk.Entry(scan_staff_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: view_staff_checker(entry_barcode))

    quit_button = tk.Button(scan_staff_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_staff_window.destroy)
    quit_button.place(x=230,y=300)

    scan_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_staff_window.mainloop()

# Here we would determine if viewing the staff in the system. (TODO: Change structure)
def view_staff_checker(entry_barcode):
    staff_json.file_checker()
    all_staffs = staff_json.retrieve_all_staffs()
    barcode = str(entry_barcode.get())
    if barcode in all_staffs:

        staff = staff_json.retrieve_staff(barcode)

        view_staff_window = tk.Tk()
        view_staff_window.title('Viewing staff in the system')
        view_staff_window.resizable(False, False)
        view_staff_window.focus_force()

        name_label = tk.Label(view_staff_window, text='Staff name: ' + str(staff['name']), font=('Helvetica', 15))
        name_label.pack()

        quit_button = tk.Button(view_staff_window, text='Quit', width=15, height=4)
        quit_button.config(command=view_staff_window.destroy)
        quit_button.pack()

        entry_barcode.delete(0, tk.END)
        view_staff_window.mainloop()

    elif barcode not in all_staffs:
        not_staff_window = tk.Tk()
        not_staff_window.title('')
        not_staff_window.geometry('300x300')
        not_staff_window.configure(background='yellow')
        not_staff_window.resizable(False, False)
        not_staff_window.focus_force()

        label = tk.Label(not_staff_window, text='Staff not in the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_staff_window, text='OK', width=20, height=5)
        ok_button.config(command=not_staff_window.destroy)
        ok_button.place(x=80,y=100)

        not_staff_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_staff_window.mainloop()


def view_card():
    scan_card_window = tk.Tk()
    scan_card_window.title('View card in the system')
    scan_card_window.geometry('400x400')
    scan_card_window.resizable(False, False)
    scan_card_window.focus_force()

    label = tk.Label(scan_card_window, text='Scan card code to view...', font=('Helvetica', 20))
    label.place(x=55, y=150)

    entry_barcode = tk.Entry(scan_card_window)
    entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
    entry_barcode.bind('<Return>', lambda event: view_card_checker(entry_barcode))

    quit_button = tk.Button(scan_card_window, text='Quit', width=20, height=5)
    quit_button.config(command=scan_card_window.destroy)
    quit_button.place(x=230,y=300)

    scan_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
    scan_card_window.mainloop()

# Here we would determine if viewing the card in the system. (TODO: Change structure)
def view_card_checker(entry_barcode):
    credit_json.file_checker()
    all_cards = credit_json.retrieve_all_cards()
    barcode = str(entry_barcode.get())
    if barcode in all_cards:

        card = credit_json.retrieve_card(barcode)

        view_card_window = tk.Tk()
        view_card_window.title('Viewing card in the system')
        view_card_window.resizable(False, False)
        view_card_window.focus_force()

        name_label = tk.Label(view_card_window, text='Name: ' + str(card['name']), font=('Helvetica', 15))
        name_label.pack()

        credit_label = tk.Label(view_card_window, text='Credit: ' + str(card['credit']), font=('Helvetica', 15))
        credit_label.pack()

        quit_button = tk.Button(view_card_window, text='Quit', width=15, height=4)
        quit_button.config(command=view_card_window.destroy)
        quit_button.pack()

        entry_barcode.delete(0, tk.END)
        view_card_window.mainloop()

    elif barcode not in all_cards:
        not_card_window = tk.Tk()
        not_card_window.title('')
        not_card_window.geometry('300x300')
        not_card_window.configure(background='yellow')
        not_card_window.resizable(False, False)
        not_card_window.focus_force()

        label = tk.Label(not_card_window, text='Card not in the system', font=('Helvetica', 16))
        label.place(x=45,y=30)

        ok_button = tk.Button(not_card_window, text='OK', width=20, height=5)
        ok_button.config(command=not_card_window.destroy)
        ok_button.place(x=80,y=100)

        not_card_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        entry_barcode.delete(0, tk.END)
        not_card_window.mainloop()



# View all things here
def view_all_items():

    all_items_window = tk.Tk()
    all_items_window.title('View all items')
    all_items_window.resizable(False,False)
    all_items_window.focus_force()
    
    label = tk.Label(all_items_window, text='All Items', font=('Helvetica', 20))
    label.pack()

    text_box = tk.Text(all_items_window, font=("Helvetica", 20))

    all_items = item_json.retrieve_all_items()

    for barcode in all_items:
        text_box.insert(tk.END,'Name: ')
        text_box.insert(tk.END, str(all_items[barcode]['name']) + '\n')
        text_box.insert(tk.END,'Price: ')
        text_box.insert(tk.END, str(all_items[barcode]['price']) + '\n')
        text_box.insert(tk.END,'Section: ')
        text_box.insert(tk.END, str(all_items[barcode]['section']) + '\n')
        text_box.insert(tk.END,'barcode: ')
        text_box.insert(tk.END, str(all_items[barcode]['barcode']) + '\n')
        text_box.insert(tk.END,'Quantity: ')
        text_box.insert(tk.END, str(all_items[barcode]['quantity']) + '\n')
        text_box.insert(tk.END, "===========================================\n")

    text_box.config(state=tk.DISABLED)
    text_box.pack()

    quit_button = tk.Button(all_items_window, text='Quit', width=20, height=5)
    quit_button.config(command=all_items_window.destroy)
    quit_button.pack()

    all_items_window.mainloop()


def view_all_staffs():

    all_staffs_window = tk.Tk()
    all_staffs_window.title('View all staffs')
    all_staffs_window.resizable(False,False)
    all_staffs_window.focus_force()
    
    label = tk.Label(all_staffs_window, text='All Staffs', font=('Helvetica', 20))
    label.pack()

    text_box = tk.Text(all_staffs_window, font=("Helvetica", 20))

    all_staffs = staff_json.retrieve_all_staffs()

    for barcode in all_staffs:
        text_box.insert(tk.END,'Name: ')
        text_box.insert(tk.END, str(all_staffs[barcode]['name']) + '\n')
        text_box.insert(tk.END,'Code: ')
        text_box.insert(tk.END, str(all_staffs[barcode]['code']) + '\n')
        text_box.insert(tk.END, "===========================================\n")

    text_box.config(state=tk.DISABLED)
    text_box.pack()

    quit_button = tk.Button(all_staffs_window, text='Quit', width=20, height=5)
    quit_button.config(command=all_staffs_window.destroy)
    quit_button.pack()

    all_staffs_window.mainloop()

def view_all_cards():

    all_cards_window = tk.Tk()
    all_cards_window.title('View all credit cards')
    all_cards_window.resizable(False,False)
    all_cards_window.focus_force()
    
    label = tk.Label(all_cards_window, text='All Cards', font=('Helvetica', 20))
    label.pack()

    text_box = tk.Text(all_cards_window, font=("Helvetica", 20))

    all_cards = credit_json.retrieve_all_cards()

    for barcode in all_cards:
        text_box.insert(tk.END,'Name: ')
        text_box.insert(tk.END, str(all_cards[barcode]['name']) + '\n')
        text_box.insert(tk.END,'Code: ')
        text_box.insert(tk.END, str(all_cards[barcode]['code']) + '\n')
        text_box.insert(tk.END,'Credit: ')
        text_box.insert(tk.END, str(all_cards[barcode]['credit']) + '$\n')
        text_box.insert(tk.END, "===========================================\n")

    text_box.config(state=tk.DISABLED)
    text_box.pack()

    quit_button = tk.Button(all_cards_window, text='Quit', width=20, height=5)
    quit_button.config(command=all_cards_window.destroy)
    quit_button.pack()

    all_cards_window.mainloop()



