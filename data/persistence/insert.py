import sqlite3


def get_bot_from_user():
    print("Please enter name of bot:")
    name = input()
    print("Please enter maximum speed:")
    speed = int(input())
    print("Please enter maximum strength:")
    strength = int(input())
    print("Please enter the manufacture date:")
    date = input()
    print("Please enter the manufacture id:")
    id = int(input())
    return [name, speed, strength, date, id]


def insert_bot_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql = "INSERT INTO bots" \
        "(name, max speed, max strength, date)"\
            "VALUES" \
          f"({data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]})"
    cursor.excecute(sql)
    row_id = cursor.lastrowid
    db.close()
    print(f"ID of new row is{row_id}")


def run():
    data = get_bot_from_user()
    insert_bot_in_db(data)


run()
