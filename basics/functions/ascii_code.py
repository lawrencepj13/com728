print("Program Started!")
print("Please enter a letter")
letter = input()
if len(letter) == 1:
    print(f"The ASCII code for {letter} is {ord(letter)}")
else:
    print("A single character was expected")
print("The program has ended.")