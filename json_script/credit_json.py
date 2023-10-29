import json

file_path = 'json_script/json/credit.json'

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


# Add a new card to the json_file.
def add_card(code, name, credit):
    global json_data

    new_card = {
        'name' : name,
        'code' : code,
        'credit' : credit
    }

    json_data[code] = new_card

    # Write the updated data
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Remove a card from the database.
def remove_card(code):
    global json_data
    del json_data[str(code)]

    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Update credits of a card, they could or remove
def update_card(code, name, credit):
    global json_data

    json_data[str(code)]['name'] = name
    json_data[str(code)]['credit'] = credit

    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Return all staff members in the json database
def retrieve_all_cards():
    global json_data
    return json_data


file_checker()

#UNIT TESTING
#code = 8113244
#add_card(code, 'John Doe', 11111)
#remove_card(code)
#update_card(code, 'John Doe', 111 - 100)
#all_cards = retrieve_all_cards()