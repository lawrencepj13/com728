print("How many cables must I avoid?")
cables_to_avoid = int(input())
print()
live_cables = 0
print()
while cables_to_avoid > live_cables:
    print("Avoiding...", end="")
    live_cables = live_cables + 1
    print(f"Done! {live_cables} to avoid!")

print()
print("All live cables have been avoided")