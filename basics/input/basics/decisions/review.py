print("Welcome hero, your adventure begins now. What path will you take? (left, right, straight ahead or behind?)")
path = input()
if path == "left":
    print("You come across a river - will you cross or leave?")
    decision = input()
    if decision == "leave":
        print("You return to the start")
    elif decision == "cross":
        print("You cross the treacherous waters")
    else:
        print("Try again adventurer")
elif path == "right":
    print("You come across a fort - will you enter?")
    enter = input()
    if enter == "yes":
        print("You enter the fort - what do you see?")
        sight = input()
        print("What do you smell?")
        smell = input()
        if (sight == "ogre") and (smell == "foul"):
            print("You prepare for battle!")
        else:
            print("You continue into the fort")
    elif enter == "no":
        print("You return to the path")
    else:
        print("Try again adventurer")
elif path == "straight ahead":
    print("You reach a forest and find a sword - How long is the sword?")
    length = input()
    if (length == "long") or (length == "short"):
        print("This sword will do the job!")
    else:
        print("This sword is not worthy - you discard it")
elif path == "behind":
    print("You turn around and see a great mountain - Will you take the long or the short path?")
    mountain_path = input()

else:
    print("You need to select a path!")
