from json_script import item_json
import tkinter as tk


# Keep references to the widgets
name_label = None
entry_name = None
price_label = None
entry_price = None
section_label = None
entry_section = None
quantity_label = None
entry_quantity = None
save_button = None
create_labels_buttons = True

# Retrieve all items in the json file
all_items = item_json.retrieve_all_items()


def add_item():
    add_item_window = tk.Tk()
    add_item_window.title('Adding Item')
    add_item_window.geometry('1000x1000')
    add_item_window.resizable(False,False)
    add_item_window.focus_force()

    barcode_label = tk.Label(add_item_window, text='Barcode')
    barcode_label.pack()
    entry_barcode = tk.Entry(add_item_window)
    entry_barcode.pack()


    submit_button = tk.Button(add_item_window, text='Submit', command=lambda: check_barcode(entry_barcode, add_item_window))
    submit_button.pack()


    add_item_window.mainloop()


def check_barcode(entry_barcode, add_item_window):
    global name_label, entry_name, price_label, entry_price, section_label, entry_section, quantity_label, entry_quantity, create_labels_buttons, save_button
    if (entry_barcode.get() not in all_items) and entry_barcode.get() != '' and create_labels_buttons:
        name_label = tk.Label(add_item_window, text='Product name')
        name_label.pack()
        entry_name = tk.Entry(add_item_window)
        entry_name.pack()

        price_label = tk.Label(add_item_window, text='Price of product')
        price_label.pack()
        entry_price = tk.Entry(add_item_window)
        entry_price.pack()

        section_label = tk.Label(add_item_window, text='Section')
        section_label.pack()
        entry_section = tk.Entry(add_item_window)
        entry_section.pack()

        quantity_label = tk.Label(add_item_window, text='Quantity')
        quantity_label.pack()
        entry_quantity = tk.Entry(add_item_window)
        entry_quantity.pack()

        create_labels_buttons = False

        save_button = tk.Button(add_item_window, text='Save', command=lambda: add_item_to_json(entry_barcode.get(), add_item_window))
        save_button.pack()
        
    elif entry_barcode.get() in all_items:
        if name_label:
            name_label.destroy()
        if entry_name:
            entry_name.destroy()
        if price_label:
            price_label.destroy()
        if entry_price:
            entry_price.destroy()
        if section_label:
            section_label.destroy()
        if entry_section:
            entry_section.destroy()
        if quantity_label:
            quantity_label.destroy()
        if entry_quantity:
            entry_quantity.destroy()
        if save_button:
            save_button.destroy()

        create_labels_buttons = True


def add_item_to_json(barcode, add_item_window):
    global entry_name, entry_price, entry_section, entry_quantity

    name = entry_name.get()
    # TODO: make sure there is no negative number
    price = round(float(entry_price.get()), 2)
    section = str(entry_section.get())
    # TODO: make sure there is no negative number
    quantity = int(entry_quantity.get())
    item_json.add_item(barcode, name, price, section, quantity)
    add_item_window.destroy()
        

def retrieve_item(barcode):
    return item_json.retrieve_item(barcode)



















def remove_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        item_json.remove_item(barcode)

    elif str(barcode) not in all_items:
        print('Error, this barcode is not in the system!!!')


def update_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        name = input('Enter new? name of the product: ')
        # TODO: make sure there is no negative number
        price = round(float(input('Enter new? price of product: ')), 2)
        section = str(input('Enter new? section of the product: '))
        # TODO: make sure there is no negative number
        quantity = int(input('Modify? quantity of the item: '))
        item_json.update_item(barcode, name, price, section, quantity)

    elif str(barcode) not in all_items:
        print('Error, this barcode is not in the system')


def view_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        #TESTING FOR GUI WITH TKINTER
        item = item_json.retrieve_item(barcode)
        #return item_json.retrieve_item(barcode)

    #elif str(barcode) not in all_items:
        #print('Barcode is not in the system!!!')