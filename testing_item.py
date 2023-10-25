from json_script import item_json

def choices():
    print('press 1 to add item')
    print('press 2 to remove item')
    print('press 3 to update an item')
    print('press 4 to view an item') # scan item to find it
    print('Press \'q\' to quit') 


# Get all items inside the json file
all_items = item_json.retrieve_all_items()


def add_item():
    barcode = int(input('Enter barcode: '))
    name = input('Enter name of the product: ')
    price = float(input('Enter price of product: '))
    section = str(input('Enter section of the product: '))
    quantity = int(input('Enter quantity of the item: '))
    item_json.add_item(barcode, name, price, section)

choices()
word = input().lower()

while word != 'q':
    if word == '1':
        add_item()
    
    choices()
    word = input().lower()