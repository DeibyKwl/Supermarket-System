from json_script import item_json
from services import item_services

# TODO: implement the gui for this function

def choices():
    print('press 1 to add item')
    print('press 2 to remove item')
    print('press 3 to update an item')
    print('press 4 to view an item') # scan item to find it
    print('press 5 to view all items')
    print('Press \'q\' to quit') 


# Get all items inside the json file
all_items = item_json.retrieve_all_items()


"""choices()
word = input().lower()

while word != 'q':
    if word == '1':
        item_services.add_item(all_items)
    if word == '2':
        item_services.remove_item(all_items)
    if word == '3':
        item_services.update_item(all_items)    
    if word == '4':
        item = item_services.view_item(all_items)
        print(item)
    if word =='5':
        print(all_items)

    choices()
    word = input().lower()"""