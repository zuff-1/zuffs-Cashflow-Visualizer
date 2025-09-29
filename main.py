# v0.2.11
# full rewrite with classes

import sys
import os

def function_clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def function_enter_to_continue():
    input("\nPress Enter to continue...")

def function_exit_program():
    function_clear_screen()
    print("Thanks for using the program! :)")
    input("Press Enter one more time to exit.")
    sys.exit()

def function_safe_number_input(prompt_text):
    while True:
        try:
            value = float(input(prompt_text))
            return value
        except ValueError:
            print("Invalid input, please enter a valid number.")

class class_item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class class_storage:

    def __init__ (self):
        self.items = []
        self.price_history = []
        self.quantity_history = []
    
    def method_add_item(self, name, quantity, price):
        for row_index, item_name in enumerate(self.items):
            if item_name[0] == name:
                self.items[row_index][1] += quantity
                self.items[row_index][2] += quantity * price
                self.price_history[row_index].append(price)
                self.quantity_history[row_index].append(quantity)
                return
        self.quantity_history.append([name, quantity])
        self.price_history.append([name, price])
        self.items.append([name, quantity, quantity * price])
    
    def method_price_list_and_history(self):
        function_clear_screen()
        print("\n\n====Price List and History====\n")
        print("Item Name | Price 1, Price 2, ...")
        for row_index, item_name in enumerate(self.price_history):
            print(f"{row_index+1}. {item_name[0]} | {item_name[1:]}")
        function_enter_to_continue()
        display1.method_choice_menu1()
    
    def method_total_price_and_quantity(self):
        function_clear_screen()
        print("\n\n====Total Price and Quantity====\n")
        print("Item Name | Total Quantity | Total Price")
        for row_index, item_name in enumerate(self.items):
            print(f"{row_index+1}. {item_name[0]} | {item_name[1]} | {item_name[2]:.2f}$")
        function_enter_to_continue()
        display1.method_choice_menu1()

storage1 = class_storage()

class class_display:

    def method_intro1(self):
        function_clear_screen()
        print("\n\n\n\n\n\n====Welcome to zuff's price calculator!====\n\n"
                "Type /done when you're done adding items. \n")
        function_enter_to_continue()
    
    def method_user_input1(self):
        while True:
            function_clear_screen()
            name = input("\n===========================================\n\n"
                         "Enter item name: ")
            if name == "/done":
                break
            quantity = function_safe_number_input("Enter item quantity: ")
            price = function_safe_number_input("Enter item price: ")
            storage1.method_add_item(name, quantity, price)
    
    def method_choice_menu1(self):
        while True:
            function_clear_screen()
            print("\n\n============Menu============\n\n"
                    "Choose Option: \n\n"
                    "1. Price list and history\n"
                    "2. Total price and quantity\n"
                    "3. Input more items\n"
                    "4. Exit program")
            choice = int(input("\nEnter choice (1-4): "))
            if choice == 1:
                storage1.method_price_list_and_history()
            elif choice == 2:
                storage1.method_total_price_and_quantity()
            elif choice == 3:
                self.method_user_input1()
            elif choice == 4:
                function_exit_program()
            else:
                print("\nInvalid choice, try again.\n")

display1 = class_display()

def main_sequence():
    display1.method_intro1()
    display1.method_user_input1()
    display1.method_choice_menu1()


if __name__ == "__main__":
    main_sequence()

