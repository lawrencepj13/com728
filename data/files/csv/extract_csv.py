import csv
def extract(path):
    print("Extracting:")
    with open("bots.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done!")
    print(f"The extracted names are as follows:\n{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
