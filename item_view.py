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

#Setting Buttons
setting_button = tk.Button(root, text='Setting', width=20, height=5)
setting_button.config(command=settings_view.open_new_window)
setting_button.place(x=10,y=630)

text_box = tk.Text(root, height=15, width=40, font=('Helvetica', 20))
text_box.config(state=tk.DISABLED) # Make it read only
text_box.place(x=200, y=50)

cost_box = tk.Text(root, height=15, width=15, font=('Helvetica', 20))
cost_box.config(state=tk.DISABLED) # Make it read only
cost_box.place(x=850, y=50)

total_cost_box = tk.Text(root, height=1.3, width=15, font=('Helvetica', 20))
total_cost_box.config(state=tk.DISABLED) # Make it read only
total_cost_box.place(x=850,y=550)

# Search the item by barcode 
entry_barcode = tk.Entry(root)
#entry_barcode.place(x=1065, y=10)
entry_barcode.place(x=1281, y=721) # Place it outside the visible are to make it seem like it is hidden and still usable
entry_barcode.focus_force()

search_button = tk.Button(root, text='Search')
search_button.place(x=1200, y=8)
search_button.config(command=lambda: item_services.add_product_basket(entry_barcode, text_box, cost_box, total_cost_box))
#Here is the way to use the <return/enter> event to start function
entry_barcode.bind('<Return>', lambda event: item_services.add_product_basket(entry_barcode, text_box, cost_box, total_cost_box))



pay_button = tk.Button(root, text='Pay', background='green', width=20, height=5)
pay_button.place(x=1120,y=630)


root.mainloop()