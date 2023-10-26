from json_script import item_json


def add_item(all_items):
    
    barcode = int(input('Enter barcode: '))
    if str(barcode) not in all_items:
        name = input('Enter name of the product: ')
        # TODO: make sure there is no negative number
        price = round(float(input('Enter price of product: ')), 2)
        section = str(input('Enter section of the product: '))
        # TODO: make sure there is no negative number
        quantity = int(input('Enter quantity of the item: '))
        item_json.add_item(barcode, name, price, section)

    elif str(barcode) in all_items:
        print('Error, this barcode is already in the system!!!')


def remove_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        item_json.remove_item(barcode)

    elif str(barcode) not in all_items:
        print('Error, this barcode is not in the system!!!')


def update_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        name = input('Enter new? name of the product: ')
        # TODO: make sure there is no negative number
        price = round(float(input('Enter new? price of product: ')), 2)
        section = str(input('Enter new? section of the product: '))
        # TODO: make sure there is no negative number
        quantity = int(input('Modify? quantity of the item: '))
        item_json.update_item(barcode, name, price, section, quantity)

    elif str(barcode) not in all_items:
        print('Error, this barcode is not in the system')


def view_item(all_items):
    barcode = int(input('Enter barcode: '))
    if str(barcode) in all_items:
        return item_json.retrieve_item(barcode)

    elif str(barcode) not in all_items:
        print('Barcode is not in the system!!!')