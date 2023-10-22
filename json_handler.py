import json

file_path = 'json_data.json'

# Code to make sure there is a json file
try:
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
except FileNotFoundError:
    json_data = {}

# Add the new data to the json_file
# Example of how to use it: #add_item(12345, 'Arroz', 12.32, '3F', json_data)
def add_item(barcode, name, price, section, json_data):

    new_item = {
        'name' : name,
        'price' : price,
        'section' : section,
        'barcode' : barcode,
        'quantity' : 1
    }

    json_data[barcode] = new_item

    # Write the updated data
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


add_item(213412, 'Arro24z', 12.32, '3F', json_data)
print(json_data['12345'])
