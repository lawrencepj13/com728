def clue():
    print("Who searches for the beast?")
    user = input()
    print(f"Welcome {user} to the Black Forest") #my fave cake btw
    print("The Beast resides in its castle, deep in the forest")

def see(item):
    if item == "rose":
        print("The beast is near by!")
    else:
        print("The beast is not here!")

def dance(minutes):
    for step in range(minutes):
        print("...Dancing")
    else:
        print("The wonderful dance has come to an end...")






clue()
see("")
see("rose")
dance(3)




