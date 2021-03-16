import csv

def display_medal_tally(tally):
    with open
    tally = {}
    gold = 0
    silver = 0
    bronze = 0
    for record in records:
        if len(record[14]) > 0:
            medal = float(record[14])
            if medal == "gold":
                gold += 1
            elif medal == "silver":
                silver += 1
            else:
                bronze += 1
    tally = {"Gold", {gold}, "Silver", {silver}, "Bronze", {bronze}}
    print(tally)