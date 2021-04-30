import matplotlib.pyplot as plt


def read_data(path):
    data = []
    with open(f"{path}") as file:
        for line in file:
            data.append(float(line.strip()))
    return data


def run():
    data = read_data("tempts.txt")
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()


run()


