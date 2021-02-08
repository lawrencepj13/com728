# Script to show text input, design character and input stats
print("Welcome adventurer. What name do you go by?")
name = input()
print(f"It is nice to meet you {name}")
print()
print("You have skills on the battlefield. What class are you? - Warrior, Ranger or Mage?")
specification = input()
print(f"Very good {specification}.")
print()
print("I see you face is looking empty....")
print()
print(""""
        ------
    --         --
    --         --
    --         --
    --         -- 
       ------   
""")
print()
print("Why not give yourself some eyes?")
eyes = input()
print(f""""
        ------
    --         --
    -- {eyes}   {eyes}   --
    --         --
    --         -- 
       ------   
""")
print()
print("Wonderful. All the better to see with!")
print("How about giving yourself a mouth?")
mouth = input()
print(f""""
        ------
    --         --
    -- {eyes}   {eyes}   --
    --         --
    --   {mouth}     -- 
       ------   
""")
print()
print("Now choose your stats - You have 30 points in total")
print("Strength?")
strength = int(input())
print(f"Your Strength is {strength}")
print()
print("Dexterity?")
dexterity = int(input())
print(f"Your Dexterity is {dexterity}")
print()
print("Defense?")
defense = int(input())
print(f"Your Defense is {defense}")
print()
print("Constitution?")
const = int(input())
print(f"Your Constitution is {const}")
print()
attack_power = strength * dexterity / 2
print(f"Your offensive power is {attack_power}")
defense_power = defense * const / 2
print(f"Your defensive power is {defense_power}")
print("")
print(f"Well {name} you are looking very strong. Now protect this land as the mighty {specification} you are!")




