#define the function to identify the danger
def identify():
    print("What lies before us?")
    response = input()
    if response == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine!")
identify()
