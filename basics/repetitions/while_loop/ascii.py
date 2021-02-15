print("How many bars should be charged?")
bars_to_charge = int(input())
print()
bars_charged = 0
print()
while bars_charged < bars_to_charge:
   bars_charged = bars_charged + 1
   print(f"Charging: {'█' * bars_charged}")

print("The battery is fully charged")
