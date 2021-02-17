print("How far are we from the cave?")
steps = int(input())
print()
for count in range(steps, 0, - 1):
    print(f"{count} steps remaining!")
print()
print("We have reached the cave!")