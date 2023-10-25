from json_script import item_json

def choices():
    print('press 1 to add item')
    print('press 2 to remove item')
    print('press 3 to update an item')
    print('press 4 to view an item') # scan item to find it
    print('press 5 to add a staff')
    print('press 6 to remove a staff')
    print('press 7 to update a staff')
    print('press 8 to view staff member')
    print('Press \'q\' to quit') 


# Get all items inside the json file
all_items = item_json.retrieve_all_items()

choices()
word = input().lower()

#while word != 'q':
