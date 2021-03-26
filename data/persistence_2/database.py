import sqlite3

def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, description " \
          "FROM product " \
          "NATURAL JOIN stock"
    cursor.execute(sql)
    table = cursor.fetchall()
    print (table)
    db.close()


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.supplier_name"
    cursor.execute(sql)
    table = cursor.fetchall()
    print(table)
    db.close()


