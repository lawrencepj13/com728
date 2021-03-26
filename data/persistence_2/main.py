import sqlite3
import database

def menu():
    print("Please enter one of the following options:")
    print("""[1] Display stock levels
    [2]Display suppliers""")
    print()
    print("Your selection:")
    response = input()
    return response


def run():
    while True:
        selection = menu()
        if selection == "1":
            print(f"Your selection is {selection}")
            print()
            print("There are 3 products in the catalogue")
            print("The stock levels for each product is as follows:")
            database.display_products_with_stock_levels()
        elif selection == "2":
            print(f"Your selection is {selection}")
            print()
            print("The suppliers for each product are as follows:")
            database.display_product_supplier()
        break





run()
