import tkinter as tk
from json_script import item_json
from services import item_services

# Retrieve all items in the json file
all_items = item_json.retrieve_all_items()

# Main application window
root = tk.Tk()
root.title('Supermarket System')

# Get the screen width and height (useless for now)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window dimensions
root.geometry('1280x720')


#Labels
label = tk.Label(root, text='testing')
label.pack()

#Setting Buttons
setting_button = tk.Button(root, text='Setting')
setting_button.place(x=10,y=680)
#Practice linking button to function
setting_button.config(command=item_services.add_item(all_items))


#Text Box
text_box = tk.Text(root, wrap=tk.WORD) # wrap is use to fit the content in the width of the text box
text_box.pack()

# Set the dimensions of the Text widget
text_width = 40  # Adjust as needed
text_height = 20  # Adjust as needed
text_box.config(width=text_width, height=text_height)

# Position the Text widget on the window
text_x = 10
text_y = 10
text_box.place(x=text_x, y=text_y)

# Create a Scrollbar
scrollbar = tk.Scrollbar(root, command=text_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=scrollbar.set)


root.mainloop()