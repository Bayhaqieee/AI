# List of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Function to check if a fruit is in the list and add it if not
def add_fruit(fruit, fruits_list):
    fruit = fruit.lower()  # Convert to lowercase for case-insensitive comparison
    if fruit in fruits_list:
        print("That fruit already exists in the list")
    else:
        fruits_list.append(fruit)
        print(f"Added {fruit} to the list.")
        print("Updated list of fruits:", fruits_list)

fruit = input("Enter a fruit: ")
add_fruit(fruit, fruits)
