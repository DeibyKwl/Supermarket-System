import json

file_path = 'credit.json'

# Code to make sure there is a json file, if not create an empty json file
def file_checker():
    try:
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        json_data = {}
    
    return json_data






json_data = file_checker()