#6 user defined function - last one will get user to call one of the first 5
def display_in_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)
def display_lower(word):
    print(word.lower())
def display_upper(word):
    print(word.upper())
def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")
def repeat(word):
    print("How many times would you like the word repeated?")
    repitions = int(input())
    for repition in range(repitions):
        if(repition % 2 == 0):
            print(display_lower())
        else:
            print(display_upper())
def run():
    print("Please enter a word:")
    word = input()
    print()
    print("How would you like this word presented?")
    print("1 Display in a box")
    print("2 Display in lower case")
    print("3 Display in upper case")
    print("4 Display mirrored")
    print("5 Repeat the word")
    print("Please enter the number below:")
    response = int(input())
    if response == 1:
        display_in_box(word)
    elif response == 2:
        display_lower(word)
    elif response == 3:
        display_upper(word)
    elif response == 4:
        display_mirrored(word)
    elif response == 5:
        repeat(word)
    else:
        print("ERROR Please input correct number")
run()








