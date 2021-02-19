#define a function that counts each step and displays messages
def cross_bridge(steps):
    for step in range(steps):
        print("Crossed step")
    if steps >5:
        print("The Bridge is collapsing")
    else:
        print("We must keep going")
cross_bridge(3)
cross_bridge(6)
