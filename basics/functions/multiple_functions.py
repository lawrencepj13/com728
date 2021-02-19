#define 1 functions to show how many steps and another to read in user input
def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("***")
    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)
create_ladder()

