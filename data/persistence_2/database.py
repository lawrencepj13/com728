import sqlite3

def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, description, quantitiy " \
          "FROM product " \
          "NATURAL JOIN stock"
    cursor.execute(sql)
    table = cursor.fetchall()
    print(f"There are {len(table)} products in the catalogue:")
    print("The stock level for each product is as follows:")
    for record in table:
        print(f"Product: {record[0]}")
        print(f"Description: {record[1]}")
        print(f"Stock Level: {record[2]}")
        print()
    db.close()


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, supplier_name " \
           "FROM product " \
           "INNER JOIN supplier ON product.supplier_id = supplier.id"
    cursor.execute(sql)
    table = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    for record in table:
        print(f"Product: {record[0]}, Supplier Name: {record[1]}")
        print()

    db.close()

def display_product_supplier_location():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, supplier_name, city, country " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id " \
          "INNER JOIN  location ON supplier.location_id = location.id"
    cursor.execute(sql)
    table = cursor.fetchall()
    print("The location for each supplier are as follows:")
    for record in table:
        print(f"Product: {record[0]}, Supplier Name: {record[1]}, Supplier Location: {record[2]}, {record[3]}")
        print()


    db.close()


def display_product_missing_suppliers():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, supplier_name " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id " \

    cursor.execute(sql)
    table = cursor.fetchall()
    print("The location for each supplier are as follows:")
    for record in table:
        print(f"Product: {record[0]}, Supplier Name: {record[1]}")
        print()


    db.close()


def display_suppliers_missing_products():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, supplier_name " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier.id " \

    cursor.execute(sql)
    table = cursor.fetchall()
    print("The location for each supplier are as follows:")
    for record in table:
        print(f"Product: {record[0]}, Supplier Name: {record[1]}")
        print()


    db.close()


def display_missing_data():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, supplier_name " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier.id " \
          "SELECT name, supplier_name, city, location " \
          "FROM product " \
          "LEFT OUTER JOIN location ON supplier.location_id = location.id " \

    cursor.execute(sql)
    table = cursor.fetchall()
    missing_supplier = []
    missing_product = []
    missing_location = []
    for record in table:
        if record[0] == None:
            missing_product.append(record)
        elif record[1] == None:
            missing_supplier.append(record)
        elif record[2, 3] == None:
            missing_location.append(record)
    print(f"The following products are missing suppliers: {missing_product}")
    print()
    print(f"The following suppliers are missing products: {missing_supplier}")
    print()
    print(f"The following locations do not have a supplier: {missing_location}")

    db.close()