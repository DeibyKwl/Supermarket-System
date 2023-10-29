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

total_cost = 0 # Use to calculate total cost of basket
basket = {} # This will be the dictionary holding scanned items

# Retrieve all items in the json file
all_items = item_json.retrieve_all_items()
        

def retrieve_item(barcode):
    return item_json.retrieve_item(barcode)


def add_product_basket(entry_barcode, text_box, cost_box, total_cost_box):
    
    global total_cost, basket
    all_items = item_json.retrieve_all_items()
    if entry_barcode.get() in all_items:
        product = retrieve_item(entry_barcode.get())
        # Make sure the product has enough quantity
        if product['quantity'] > 0:
        
            text_box.config(state=tk.NORMAL)
            text_box.insert(tk.END, product['name'] + '\n')
            text_box.see(tk.END)
            text_box.config(state=tk.DISABLED)
            
            entry_barcode.delete(0, tk.END)
            update_item(product)

            cost_box.config(state=tk.NORMAL)
            cost_box.insert(tk.END, '$' + str(round(product['price'], 2)) + '\n')
            cost_box.see(tk.END)
            cost_box.config(state=tk.DISABLED)

            total_cost += product['price']
            total_cost_box.config(state=tk.NORMAL)
            if total_cost != 0: # Update the total_cost by deleting previous total_cost
                total_cost_box.delete(1.0, tk.END)
            total_cost_box.insert(tk.END, '$' + str(round(total_cost, 2)) + '\n')
            total_cost_box.config(state=tk.DISABLED)

            #basket[product['name']] = round(product['price'], 2)
            

    elif entry_barcode.get() not in all_items:
        #TODO give an error message
        entry_barcode.delete(0, tk.END)


def clear_product_basket(text_box, cost_box, total_cost_box):
    global total_cost, basket
    total_cost = 0
    basket = {}

    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.config(state=tk.DISABLED)

    cost_box.config(state=tk.NORMAL)
    cost_box.delete(1.0, tk.END)
    cost_box.config(state=tk.DISABLED)

    total_cost_box.config(state=tk.NORMAL)
    total_cost_box.delete(1.0, tk.END)
    total_cost_box.config(state=tk.DISABLED)







def remove_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        item_json.remove_item(barcode)

    elif str(barcode) not in all_items:
        print('Error, this barcode is not in the system!!!')


def update_item(product):
    #barcode = int(input('Enter barcode: '))
    #if str(barcode) in all_items:
        #name = input('Enter new? name of the product: ')
        # TODO: make sure there is no negative number
        #price = round(float(input('Enter new? price of product: ')), 2)
        #section = str(input('Enter new? section of the product: '))
        # TODO: make sure there is no negative number
        #quantity = int(input('Modify? quantity of the item: '))
    item_json.update_item(product['barcode'], product['name'], product['price'], product['section'], product['quantity'] - 1)

    #elif str(barcode) not in all_items:
    #    print('Error, this barcode is not in the system')


def view_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        #TESTING FOR GUI WITH TKINTER
        item = item_json.retrieve_item(barcode)
        #return item_json.retrieve_item(barcode)

    #elif str(barcode) not in all_items:
        #print('Barcode is not in the system!!!')