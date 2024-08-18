# Function to determine grade based on score
def determine_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    elif 0 <= score <= 49:
        return 'F'
    else:
        return 'Invalid score'

score = int(input("Enter your score: "))
grade = determine_grade(score)
print(f"Your grade is: {grade}")
