import sqlite3


def display_presenters_with_orgs():
    db = sqlite3.connect("events.db")
    cursor = db.cursor()
    sql = "SELECT presenter_name, organisation_name " \
          "FROM presenters " \
          "INNER JOIN presenterorgs ON presenters.organisationid = presenterorgs.id"
    cursor.execute(sql)
    table = cursor.fetchall()
    print("Presenter names and organisations are as follows:")
    for record in table:
        print(f"Presenter Name: {record[0]}")
        print(f"Organisation Name: {record[1]}")
        print()
    db.close()

