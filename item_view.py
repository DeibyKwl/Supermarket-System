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

#Setting Buttons
setting_button = tk.Button(root, text='Setting', command=top_level_view_item.open_new_window, width=20, height=5)
setting_button.place(x=10,y=630)


root.mainloop()