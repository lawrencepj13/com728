import sqlite3
import database

def menu():
    print("Please enter one of the following options:")
    print("""[1] Display stock levels
    [2]Display suppliers
    [3] Display supplier location
    [4] Display products with missing suppliers
    [5] Display suppliers with missing products
    [6] Display missing data""")
    print()
    print("Your selection:")
    response = int(input())
    return response


def run():
    selection = menu()
    if selection == 1:
            print(f"Your selection is {selection}")
            database.display_products_with_stock_levels()
    elif selection == 2:
            print(f"Your selection is {selection}")
            database.display_product_supplier()
    elif selection == 3:
        print(f"Your selection is {selection}")
        database.display_product_supplier_location()
    elif selection == 4:
        print(f"Your selection is {selection}")
        database.display_product_missing_suppliers()
    elif selection == 5:
        database.display_suppliers_missing_products()
    elif selection == 6:
        database.display_missing_data()
    else:
        print("Invalid selection")






run()
