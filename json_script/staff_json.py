import json

file_path = 'json_script/json/staff.json'

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

# Add a new staff member to the json_file.
def add_staff(code, name):
    global json_data

    new_staff = {
        'name' : name,
        'code' : code
    }

    json_data[code] = new_staff

    # Write the updated data
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Remove an staff member from the database.
def remove_staff(code):
    global json_data
    del json_data[str(code)]

    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Update info from staff member
# You are expected to use as parameters all attr of a staff
# even if they don't change anything
def update_staff(code, name):
    global json_data

    json_data[str(code)]['name'] = name

    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


# Return all staff members in the json database
def retrieve_all_staffs():
    global json_data
    return json_data

def retrieve_staff(code):
    global json_data
    return json_data[str(code)]

file_checker()

#UNIT TESTING
#code = 1232
#add_staff(code, "John Doe")
#remove_staff(code)
#update_staff(code, 'John Cena')
#all_staffs = retrieve_all_staffs()