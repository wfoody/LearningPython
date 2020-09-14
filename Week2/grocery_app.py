# Grocery Store App

Master_List = []
stores = []
items = []

def add_store():
    storeName = input("Enter store name: ")
    storeAddress = input("Enter store address: ")
    grocery_store = GroceryStore(storeName, storeAddress)
    stores.append(grocery_store)

def add_item():
    itemName = input("Enter item name: ")
    itemPrice = input("Enter item price: $")
    itemQuantity = input("Enter item quantity: ")
    item = Item(itemName, itemPrice, itemQuantity)
    items.append(item)

def view_list():
    print(stores)


class GroceryStore:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = [] 

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def menu():
    while True:
        choice = input("""
            Please choose one of the following options by entering a number:

            1. Add a grocery store.
            2. Add a grocery item.
            3. View list.
            4. Quit. """)

        if choice == "4":
            break

        elif choice == "1":
            add_store()

        elif choice == "2":
            add_item()

        elif choice == "3":
            view_list()

menu()
