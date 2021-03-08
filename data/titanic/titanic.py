import csv


records = []
headings = []

def load_data(file_path):
    print("Loading Data...")
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        records = len(list(csv_reader))
        print("Done!")
        return records



def run():
    file = load_data("titanic.csv")
    num_records = records
    records.append(load_data("titanic.csv"))
    print(f"Succesfully loaded {num_records} records.")



if __name__ == "__main__":
    run()
