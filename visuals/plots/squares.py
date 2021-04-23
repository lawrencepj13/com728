import matplotlib.pyplot as plt

def small():
    x = [3, 4, 4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, 'or--')


def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, 'sg--')


def large():
    x = [0, 6, 6, 0, 0]
    y = [0, 0, 6, 6, 0]
    plt.plot(x, y, 'pb-')


def run():
    small()
    medium()
    large()
    plt.show()


run()

