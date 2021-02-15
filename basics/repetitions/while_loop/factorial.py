print("Please enter a number:")
number = int(input())
print()
count = 0
total = 1
while count < number:
    count = count + 1
    total = total * count
print(f"The factorial is {total}")


