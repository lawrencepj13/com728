import csv
import matplotlib.pyplot as plt


def read_data():
    with open("temps.csv") as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader)
        data = {'survived': [], 'sex': [], 'age': [], 'fare': []}

        for line in csv_reader:
            survived = line[1].strip()
            sex = line[14].strip()
            age = line[4].strip()
            fare = line[8].strip()


            if (survived != "" and sex != "" and age != "" and fare != ""):
                data['survived'].append(bool(int(survived)))

                if (int(sex) == 0):
                    data['sex'].append('male')
                else:
                    data['sex'].append('female')

                data['age'].append(float(age))
                data['fare'].append(round(float(fare), 2))

        return data



def plot_survivors_vs_sex(ax, data):
    male = {'survived': [], 'deceased': []}
    female = {'survived': [], 'deceased': []}

    for index in range(len(data['sex'])):
        sex = data['sex'][index]
        if(sex == male and data['survived'][index]):
            male ['survived'].append(sex)
        elif(sex == male and data['deceased'][index]):
            male ['deceased'].append(sex)
        elif(sex == female and data['survived'][index]):
            female ['survived'].append(sex)
        else:
            female ['deceased'].append(sex)

    labels = ['male', 'female']
    survivors = [len(male['survived']), len(female['survived'])]
    deceased = [len(male['deceased']), len(female['deceased'])]

    ax.bar(labels, survivors, label='Survived')
    ax.bar(labels, deceased, bottom=survivors, label='Deceased')
    ax.set_ylabel('sex')
    ax.legend()
    ax.set_title('Sex vs Survival')


def run():
    data = read_data()

    # plots arranged in a 2 by 2 grid
    fig, axs = plt.subplots(2, 2)

    # display plots
    plot_age_vs_survival(axs[0, 0], data)
    plot_fare_vs_survival(axs[0, 1], data)
    plot_sex_vs_survival(axs[1, 0], data)
    plot_all_vs_survival(axs[1, 1], data)

    plt.tight_layout()
    plt.show()


run()

