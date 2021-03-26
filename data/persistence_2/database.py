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


