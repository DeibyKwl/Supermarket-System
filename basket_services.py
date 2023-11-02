from json_script import item_json
import tkinter as tk

# Keep references to the widgets
"""name_label = None
entry_name = None
price_label = None
entry_price = None
section_label = None
entry_section = None
quantity_label = None
entry_quantity = None
save_button = None
create_labels_buttons = True"""

total_cost = 0 # Use to calculate total cost of basket
basket = {} # This will be the dictionary holding scanned items

# Retrieve all items in the json file
all_items = item_json.retrieve_all_items()

def add_product_basket(entry_barcode, text_box, cost_box, total_cost_box):
    
    global total_cost, basket

    all_items = item_json.retrieve_all_items()
    if entry_barcode.get() in all_items:
        product = item_json.retrieve_item(entry_barcode.get())
        # Make sure the product has enough quantity
        if product['quantity'] > 0:
        
            text_box.config(state=tk.NORMAL)
            text_box.insert(tk.END, product['name'] + '\n')
            text_box.see(tk.END)
            text_box.config(state=tk.DISABLED)
            
            entry_barcode.delete(0, tk.END)
            item_json.update_item(product['barcode'], product['name'], product['price'], product['section'], product['quantity'] - 1)

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

        entry_barcode.delete(0, tk.END)

        #TODO give an error message

        error_window = tk.Tk()
        error_window.title("Error, item not in the system")
        error_window.geometry('300x300')
        error_window.configure(background='yellow')
        error_window.resizable(False, False)
        error_window.focus_force()

        label = tk.Label(error_window, text='Sorry, item not in the system', font=('Helvetica', 16))
        label.place(x=10,y=30)

        ok_button = tk.Button(error_window, text='OK', width=20, height=5)
        ok_button.config(command=error_window.destroy)
        ok_button.place(x=80,y=100)

        error_window.mainloop()

        

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






"""
def retrieve_item(barcode):
    return item_json.retrieve_item(barcode)"""
    
"""
#MAYBE GET RID OF THIS
def remove_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        item_json.remove_item(barcode)

    elif str(barcode) not in all_items:
        print('Error, this barcode is not in the system!!!')


#MAYBE GET RID OF THIS
def update_item(product):
    #if str(barcode) in all_items:
        # TODO: make sure there is no negative number
    item_json.update_item(product['barcode'], product['name'], product['price'], product['section'], product['quantity'] - 1)

    #elif str(barcode) not in all_items:
    #    print('Error, this barcode is not in the system')


#MAYBE GET RID OF THIS
def view_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        #TESTING FOR GUI WITH TKINTER
        item = item_json.retrieve_item(barcode)
        #return item_json.retrieve_item(barcode)

    #elif str(barcode) not in all_items:
        #print('Barcode is not in the system!!!')"""