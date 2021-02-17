print("What strange markings do you see?")
markings = input()
print()
print("Identifying....")
print()
for position in range(0, len(markings), 1):
    print(f"index: {position}:", markings[position])
print()
print("Done!")

