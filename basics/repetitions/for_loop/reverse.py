print("What phrase do you see?")
phrase = input()
print()
print("Reversing...")
print("The phrase is:",end="")
for count in range(len(phrase) -1, -1, -1):
    print(phrase[count], end="")

