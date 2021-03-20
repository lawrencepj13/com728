import sqlite3


def get_bot_id_from_user():
    print("Please enter the bot id:")
    return int(input())

def display_bot_from_db(id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql = f"SELECT * FROM bots WHERE id={id}"
    cursor.execute(sql)
    record = cursor.fetchone()

    db.close()
    print(record)


def get_bot_details_from_users():
    print("What would you like to change?")
    change = input()
    print(f"What is the new value for {change}?")
    changes = input()
    return [change, changes]


def update_bot_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = f"UPDATE bots SET {data[0]} = '{data[1]}'"
    cursor.execute(sql)

    db.commit()
    print("Updated")


def run():
    id = get_bot_id_from_user()
    display_bot_from_db(id)
    data = get_bot_details_from_users()
    update_bot_in_db(data)


run()


