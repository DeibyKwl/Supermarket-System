from json_script import item_json
from json_script import credit_json
import tkinter as tk

total_cost = 0 # Use to calculate total cost of basket
basket_num = {}
basket = item_json.retrieve_all_items()
barcode_scanned = set() # Hold the barcode that were scanned

# Retrieve all items in the json file
all_items = item_json.retrieve_all_items()

def set_focus(event, entry_barcode):
    # Check if the focus should be set to entry_barcode
    if event.widget != entry_barcode:
        entry_barcode.focus_set()

def add_product_basket(entry_barcode, text_box, cost_box, total_cost_box):
    
    global total_cost, basket, basket_num, barcode_scanned

    all_items = item_json.retrieve_all_items()
    if (entry_barcode.get() in all_items):
        product = item_json.retrieve_item(entry_barcode.get())
        # Make sure the product has enough quantity
        if product['quantity'] > 0:
            
            if str(entry_barcode.get()) not in barcode_scanned:
                barcode_scanned.add(str(entry_barcode.get()))
                basket_num[str(entry_barcode.get())] = 1
            else:
                basket_num[str(entry_barcode.get())] += 1

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

        elif product['quantity'] == 0:
            entry_barcode.delete(0, tk.END)

            error_window = tk.Tk()
            error_window.title("Error, no more of this item")
            error_window.geometry('300x300')
            error_window.configure(background='yellow')
            error_window.resizable(False, False)
            error_window.focus_force()

            label = tk.Label(error_window, text='Sorry, no more of this item', font=('Helvetica', 16))
            label.place(x=10,y=30)

            ok_button = tk.Button(error_window, text='OK', width=20, height=5)
            ok_button.config(command=error_window.destroy)
            ok_button.place(x=80,y=100)

            error_window.mainloop()


    elif entry_barcode.get() not in all_items:

        entry_barcode.delete(0, tk.END)

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
    global total_cost, basket, basket_num, barcode_scanned

    for barcode in barcode_scanned:
        item_json.update_item(barcode, basket[barcode]['name'], basket[barcode]['price'], basket[barcode]['section'], basket[barcode]['quantity'] + basket_num[barcode])


    total_cost = 0
    barcode_scanned = set()
    basket_num = {}
    basket = item_json.retrieve_all_items() # Reset the basket

    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.config(state=tk.DISABLED)

    cost_box.config(state=tk.NORMAL)
    cost_box.delete(1.0, tk.END)
    cost_box.config(state=tk.DISABLED)

    total_cost_box.config(state=tk.NORMAL)
    total_cost_box.delete(1.0, tk.END)
    total_cost_box.config(state=tk.DISABLED)


def pay_product_basket(text_box, cost_box, total_cost_box):
    global total_cost, basket, basket_num, barcode_scanned
    # To make sure the pay button does not activate the card prompt if the basket is empty
    if total_cost > 0: 
        pay_window = tk.Tk()
        pay_window.resizable(False, False)
        pay_window.title('Payment window')
        pay_window.geometry('400x400')
        pay_window.focus_force()

        scan_label = tk.Label(pay_window, text='Scan your card...', font=('Helvetica', 20))
        scan_label.place(x=90, y=150)

        entry_barcode = tk.Entry(pay_window)
        entry_barcode.place(x=401, y=401) # Place it outside the visible are to make it seem like it is hidden and still usable
        entry_barcode.bind('<Return>', lambda event: pay_checker(entry_barcode, pay_window, text_box, cost_box, total_cost_box))

        cancel_button = tk.Button(pay_window, text='Cancel', width=20, height=5)
        cancel_button.config(command=pay_window.destroy)
        cancel_button.place(x=230,y=300)

        pay_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))

        pay_window.mainloop()


def pay_checker(entry_barcode, pay_window, text_box, cost_box, total_cost_box):
    global total_cost, basket, basket_num, barcode_scanned
    barcode = entry_barcode.get()
    entry_barcode.delete(0, tk.END) # Delete previous input for new barcode input
    all_card_credits = credit_json.retrieve_all_cards()

    # Make sure the card is in the system
    if str(barcode) in all_card_credits:
        card = all_card_credits[str(barcode)]
        
        avail_credit = card['credit']

        if avail_credit >= total_cost:
            pay_window.destroy()

            card_info_window = tk.Tk()
            card_info_window.resizable(False, False)
            card_info_window.focus_force()
            card_info_window.title('')
            card_info_window.geometry('500x400')

            credit_label = tk.Label(card_info_window, text=f'\nCredit available: ${avail_credit}', font=('Helvetica', 20))
            credit_label.pack()

            after_purchase = avail_credit - total_cost
            after_purchase_label = tk.Label(card_info_window, text=f'\n\nCredit after transaction: ${after_purchase}', font=('Helvetica', 20))
            after_purchase_label.pack()

            confirm_button = tk.Button(card_info_window, text='Confirm', width=20, height=5)
            confirm_button.config(command=lambda: payment_success(card, after_purchase, card_info_window, text_box, cost_box, total_cost_box))
            confirm_button.place(x=300,y=230)

            cancel_button = tk.Button(card_info_window, text='Cancel', width=20, height=5)
            cancel_button.config(command=card_info_window.destroy)
            cancel_button.place(x=80,y=230)

        elif avail_credit < total_cost:
            not_enough_window = tk.Tk()
            not_enough_window.title('')
            not_enough_window.geometry('300x300')
            not_enough_window.configure(background='yellow')
            not_enough_window.resizable(False, False)
            not_enough_window.focus_force()

            label = tk.Label(not_enough_window, text=f'Not enough credit\n\nAvailable credit: ${avail_credit}', font=('Helvetica', 16))
            label.place(x=45,y=20)

            ok_button = tk.Button(not_enough_window, text='OK', width=20, height=5)
            ok_button.config(command=not_enough_window.destroy)
            ok_button.place(x=80,y=120)

            not_enough_window.bind('<FocusIn>', lambda event: set_focus(event, entry_barcode))
            not_enough_window.mainloop()

    elif str(barcode) not in all_card_credits:
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
        not_card_window.mainloop()


def payment_success(card, after_purchase, card_info_window, text_box, cost_box, total_cost_box):
    global total_cost, basket, basket_num, barcode_scanned

    card_info_window.destroy()
    clear_product_basket(text_box, cost_box, total_cost_box)
    credit_json.update_card(str(card['code']), card['name'], after_purchase)

    success_window = tk.Tk()
    success_window.title('')
    success_window.geometry('400x300')
    success_window.resizable(False, False)
    success_window.focus_force()

    label = tk.Label(success_window, text=f'Payment Succesful!!!\n\nYour current credit is: ${after_purchase}', font=('Helvetica', 16))
    label.place(x=70,y=20)

    close_button = tk.Button(success_window, text='Close', width=20, height=5)
    close_button.config(command=success_window.destroy)
    close_button.place(x=120,y=135)

    success_window.mainloop() 
