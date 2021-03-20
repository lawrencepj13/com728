import sqlite3



def retrieve_bot():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql_query = "SELECT * FROM bots"
    cursor.execute(sql_query)
    user_row = cursor.fetchone()
    print(user_row)
    db.close()


def run():
    retrieve_bot()


run()
