import csv
import sqlite3

def read_data_file(file_path):
    data = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            data.append(line)
    return data

def insert_to_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    for item in data:
        sql = "INSERT INTO bots" \
              "(name, max speed, max strength, date)" \
              "VALUES" \
              "(?, ?, ?, ?, ?)"

        values = [item[0], item[1], item[2], item[3], item[4]]
    cursor.execute(sql, values)

    db.commit()
    db.close()


def run():
    print("Please enter the file path:")
    response = input()
    bots_data = read_data_file(response)
    insert_to_db(bots_data)
    print("Inserting into database...")
    print("Done! 3 records inserted")




if __name__ == "__main__":
    run()