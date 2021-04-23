import matplotlib.pyplot as plt


def coordinates():
    print("Hi there! Please enter an X coordinate:")
    x = int(input())
    print("Please enter a Y coordinate:")
    y = int(input())
    return (x, y)


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinates()
        x_values.append(data)
        y_values.append(data)
        return [x_values, y_values]


def run():
    values = path()

    plt.plot(values[0], values[1], 'or--')
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()



run()




