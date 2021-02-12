print("Where should i look?")
decision = input()
if decision == "in the bedroom":
    print("where in the bedroom should I look?")
    search_bedroom = input()
    if search_bedroom == "under the bed":
        print("Found some shoes but not battery")
    else:
        print("Found some mess but no battery")
elif decision == "in the bathroom":
    print("Where in the bathroom should I look?")
    search_bathroom = input()
    if search_bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")
elif decision == "in the lab":
    print("Where in the lab should I look?")
    search_lab = input()
    if search_lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")
else:
    print("I do not know where that is but I will keep looking!")