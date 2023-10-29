import json

file_path = 'json_script/json/item.json'

json_data = None

# Code to make sure there is a json file, if not create an empty json file
def file_checker():
    global json_data
    try:
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        json_data = {}
    
    #return json_data

# Add the new data to the json_file.
# Example of how to use it: #add_item(12345, 'Arroz', 12.32, '3F', json_data)
def add_item(barcode, name, price, section, quantity):
    global json_data
    new_item = {
        'name' : name,
        'price' : price,
        'section' : section,
        'barcode' : barcode,
        'quantity' : quantity
    }

    json_data[barcode] = new_item

    # Write the updated data
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Remove an item from the database.
def remove_item(barcode):
    global json_data
    del json_data[str(barcode)]

    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Update attribute of the item
# You are expected to use as parameters all attr of item
# even if they don't change anything
def update_item(barcode, name, price, section, quantity):
    global json_data

    json_data[str(barcode)]['name'] = name
    json_data[str(barcode)]['price'] = price
    json_data[str(barcode)]['section'] = section
    json_data[str(barcode)]['quantity'] = quantity

    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Return all the items in the json database
def retrieve_all_items():
    global json_data
    return json_data

# Return specific item by barcode
def retrieve_item(barcode):
    global json_data
    return json_data[str(barcode)]


file_checker() # Reread the json file searching for any update


# UNIT TESTING
#barcode = '079400457561'
#add_item(barcode, 'Arroz', 12.32, '3F', json_data)
#remove_item(barcode)
#update_item(barcode, 'Queso', 50.10, '9C', 10)
#all_items = retrieve_all_items()
#item = retrieve_item(barcode)
#print(all_items)