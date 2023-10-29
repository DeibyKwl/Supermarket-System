import tkinter as tk
from json_script import item_json
import item_services
import settings_view

# Retrieve all items in the json file
all_items = item_json.retrieve_all_items()

# Main application window
root = tk.Tk()
root.title('Supermarket System')

# Set the window dimensions
root.geometry('1280x720')
root.resizable(False,False)

scan_label = tk.Label(root, text='Scan Items...', font=('Helvetica', 20))
scan_label.place(x=400,y=8)

# Creation of scrollbar here, functionalities added later
text_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, width=55)

# Text boxes here...
text_box = tk.Text(root, height=15, width=40, font=('Helvetica', 20), yscrollcommand=text_scrollbar.set)
text_box.config(state=tk.DISABLED) # Make it read only
text_box.place(x=200, y=50)

cost_box = tk.Text(root, height=15, width=15, font=('Helvetica', 20), yscrollcommand=text_scrollbar.set)
cost_box.config(state=tk.DISABLED) # Make it read only
cost_box.place(x=850, y=50)

total_cost_box = tk.Text(root, height=1.3, width=15, font=('Helvetica', 20))
total_cost_box.config(state=tk.DISABLED) # Make it read only
total_cost_box.place(x=850,y=550)

# Search the item by barcode 
entry_barcode = tk.Entry(root)
entry_barcode.place(x=1281, y=721) # Place it outside the visible are to make it seem like it is hidden and still usable
#Here is the way to use the <return/enter> event to start function
entry_barcode.bind('<Return>', lambda event: item_services.add_product_basket(entry_barcode, text_box, cost_box, total_cost_box))

# Setting the scrollbar here
text_scrollbar.place(x=800, y=50, height=485)
text_scrollbar.config(command=lambda *args: (text_box.yview(*args), cost_box.yview(*args)))
text_box.bind("<MouseWheel>", lambda e: "break")
cost_box.bind("<MouseWheel>", lambda e: "break")



# All buttons here...
setting_button = tk.Button(root, text='Setting', width=20, height=5)
setting_button.place(x=10,y=630)
setting_button.config(command=lambda:settings_view.security_window())

quit_button = tk.Button(root, text='Quit', width=20, height=5)
quit_button.place(x=200,y=630)
quit_button.config(command=root.destroy)

clear_button = tk.Button(root, text='Clear', background='yellow', width=20, height=5)
clear_button.place(x=1120, y=50)
clear_button.config(command=lambda: item_services.clear_product_basket(text_box, cost_box, total_cost_box))

pay_button = tk.Button(root, text='Pay', background='green', width=20, height=5)
pay_button.place(x=1120,y=630)

def set_focus(event):
    # Check if the focus should be set to entry_barcode
    if event.widget != entry_barcode:
        entry_barcode.focus_set()


root.bind('<FocusIn>', set_focus)
root.mainloop()