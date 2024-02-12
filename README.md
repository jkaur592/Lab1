# Lab1 Repository
# A function that takes an input from the user and calculate someone’s age
 
    from datetime import datetime
    def calculate_age():
    # Get current year
    current_year = datetime.now().year

    # Ask user for birth year
    birth_year = input("Enter your birth year: ")

    try:
        # Convert input to integer
        birth_year = int(birth_year)

        # Calculate age
        age = current_year - birth_year

        if age >= 0:
            print(f"You are {age} years old.")
        else:
            print("Invalid birth year. Please enter a valid year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")


calculate_age()
