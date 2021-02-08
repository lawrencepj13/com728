# Ask user to enter their name
print("What is your name human?")
name = input()
print(f"It is nice to meet you human {name}")
print("")
print("What is your age?")
user_age = int(input())
print(f"Your age is {user_age}.")
print("")
print("What is your height? (In Metres)")
user_height = float(input())
print(f"Your age is {user_height}.")
print("")
print("What is your weight? (In Kilograms")
user_weight = int(input())
print(f"Your age is {user_weight}.")
print("")
user_bmi = user_weight / (user_height**2)
print(f"{name} you are {user_age} years old and your BMI is {user_bmi}")






