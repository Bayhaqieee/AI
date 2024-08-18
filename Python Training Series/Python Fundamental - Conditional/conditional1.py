# Task 1: Check if the user is old enough to drive
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_remaining = 18 - age
    print(f"You need {years_remaining} more year{'s' if years_remaining > 1 else ''} to learn to drive.")
