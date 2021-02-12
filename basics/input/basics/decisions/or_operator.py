print("What type of adventure should I have?")
adventure = input()
# identify the adventure
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take")