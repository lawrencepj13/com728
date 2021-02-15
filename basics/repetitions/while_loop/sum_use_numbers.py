print("How many numbers should I add up?")
numbers_to_add = int(input())
added = 0
print()
total = 0
print()
while added < numbers_to_add:
    print(f"Please enter number {added} of {numbers_to_add}:")
    number = int(input())
    total = total + number
    added = added + 1
print(f"The answer is {total}")
