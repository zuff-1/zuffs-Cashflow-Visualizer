#Tuple and List Practice

import sys

storage = []



def function_storage_handler(item_type):
    for row_index, column_index in enumerate(storage):
        if column_index[0] == item_type:
            storage[row_index][1] += function_ask_for_item_price()
            return
    storage.append([item_type, function_ask_for_item_price()])
    return
                
def function_storage_display(storage):
    print("\n====Price List====\n")
    for row_index, column_index in enumerate(storage):
        print(f"{row_index+1}. {column_index[0]}: {column_index[1]}$")
    total_price = sum(column_index[1] for column_index in storage)
    print(f"\nTotal Price: {total_price}$")
    if total_price >= 100:
        print("\nA bit expensive huh? thanks for purchasing though.\n")
    else:
        print("\nToo cheap idiot, buy more.\n")

def function_end_program():
    sys.exit()



def function_ask_for_item_type():
    return input("Enter item name: ")

def function_ask_for_item_price():
    return int(input("Enter item price: "))

def function_add_item_type():
    item_type = function_ask_for_item_type()
    if item_type == "/done":
        return True
    else:
        function_storage_handler(item_type)



print("\n\n====Welcome to zuff's price calculator!====\n\n\
Type /done when you're done adding items.\n\n")
while True:
    if function_add_item_type() == True:
        break
function_storage_display(storage)
function_end_program()


















































