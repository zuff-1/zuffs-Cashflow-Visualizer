import sys

# Class representing a single item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Class representing the shopping/storage system
class Storage:
    def __init__(self):
        self.items = []  # this is a list to hold Item objects

    def add_item(self, name, price):
        # check if item already exists
        for item in self.items:
            if item.name == name:
                item.price += price
                return
        # if not found, create new Item
        self.items.append(Item(name, price))

    def display(self):
        print("\n====Price List====\n")
        total = 0
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name}: {item.price}$")
            total += item.price
        print(f"\nTotal Price: {total}$")
        if total >= 100:
            print("\nA bit expensive huh? Thanks for purchasing though.\n")
        else:
            print("\nToo cheap, buy more.\n")

    def total_price(self):
        return sum(item.price for item in self.items)

def main():
    storage = Storage()
    print("\n====Welcome to Zuff's price calculator!====\n")
    print("Type /done when you're done adding items.\n")
    
    while True:
        name = input("Enter item name: ")
        if name == "/done":
            break
        price = int(input("Enter item price: "))
        storage.add_item(name, price)

    storage.display()
    sys.exit()

if __name__ == "__main__":
    main()