import matplotlib.pyplot as plt


def data():
    print("What type of line would you like? - :, -- or -")
    line = input()
    print("What colour would you like? r, g, or b")
    colour = input()
    print("What type of marker style would you like? o, s or ^")
    marker = input()
    paths = {line, colour, marker}
    return paths



def generate():
    print("How many lines would you like to display?")
    lines = int(input())
    for line in range(lines):
        values = data()


