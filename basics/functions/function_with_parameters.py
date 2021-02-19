#define function that has 2 parameters steps remaining and steps crossed
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")
climb_ladder(5, 2)
climb_ladder(2, 5)
