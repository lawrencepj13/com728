import csv
import matplotlib.pyplot as plt


def read_data():
    with open("temps.csv") as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader)
        data = {'week 1': [], 'week 2': []}

        for line in csv_reader:
            data['week 1'].append(float(line[0].strip()))
            data['week 2'].append(float(line[1].strip()))

    return data


def run():
    data = read_data()
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.plot(range(len(['week 1'])), data['week 1'])
    # ax2.plot(range(len(['week 2'])), data['week 2'])
    # plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data['week 1'])), data['week 1'])
    ax1.set_title('week 1')
    ax1.set_ylabel('Temp')
    ax1.set_xlabel('Day')
    ax2.plot(range(len(data['week 2'])), data['week 2'])
    ax2.set_title('week 2')
    ax2.set_ylabel('Temp')
    ax2.set_xlabel('Day')
    plt.tight_layout()
    plt.show()


run()



