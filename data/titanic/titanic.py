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


def display_menu():
    print("""
      Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
  """)
    response = int(input())
    return response


def display_passenger_names():
    print("The names of the passengers are...")
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        passenger_name = ""
        for names in csv_reader:
            passenger_name += f"{names[3]}\n"
    return passenger_name




def run():
    file = load_data("titanic.csv")
    num_records = records
    records.append(load_data("titanic.csv"))
    print(f"Succesfully loaded {num_records} records.")
    menu = display_menu()
    selected_response = menu
    print(f"You have selection option: {selected_response}")
    if selected_response == 1:
        print(display_passenger_names())
    else:
        print("Error! Option not recognized!")






if __name__ == "__main__":
    run()
