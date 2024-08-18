# Function to determine the season based on the month
def determine_season(month):
    month = month.lower()  # Convert to lowercase for case-insensitive comparison
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

month = input("Enter a month: ")
season = determine_season(month)
print(f"The season is: {season}")
