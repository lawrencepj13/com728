import csv


records = []
headings = []

def load_data(file_path):
    print("Loading Data...")
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        headings.append(next(csv_reader))
        num_records = 0
        for value in csv_reader:
            records.append(value)
            num_records = num_records + 1
        print("Done!")
        return num_records


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
    for record in records:
        passenger_name = record[3]
        print(passenger_name)



def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = record[1]
        if survival_status == "1":
            num_survived += 1
    print(f"{num_survived} passengers survived")


def display_pass_gen():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1
    print(f"females: {females}, males: {males}")

def display_pass_per_age_grp():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        if len(record[5]) > 0:
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")





def run():
    num_records = load_data("titanic.csv")
    print(f"Succesfully loaded {num_records} records.")
    selected_response = display_menu()
    print(f"You have selection option: {selected_response}")
    if selected_response == 1:
        print(display_passenger_names())
    elif selected_response == 2:
        print(display_num_survivors())
    elif selected_response == 3:
        print(display_pass_gen())
    elif selected_response == 4:
        print(display_pass_per_age_grp())
    else:
        print("Error! Option not recognized!")








if __name__ == "__main__":
    run()
