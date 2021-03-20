import sqlite3



def retrieve_bot():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql_query = "SELECT * FROM bots"
    cursor.execute(sql_query)
    user_row = cursor.fetchone()
    print(user_row)
    db.close()



def retrieve_bots():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql_query = "SELECT * FROM bots"
    cursor.execute(sql_query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    db.close()

def run():
    print("Single bot in the system:")
    retrieve_bot()
    print("All bots in the system:")
    print(f"\n{retrieve_bots()}")



run()