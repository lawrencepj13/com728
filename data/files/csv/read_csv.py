import csv

def read(path):
    with open("bots.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values)
def run():
    read("bots.csv")

if __name__ == "__main__":
    run()