def helloWorld():
	print(‘Hello World’)


helloWorld()

def calculate_age():
    try:
        # Get current year
        current_year = datetime.now().year
        # Ask user for birth year
        birth_year = input("Enter your birth year: ")
        # Convert input to integer
        birth_year = int(birth_year)
        # Calculate age
        age = current_year - birth_year
        if age >= 0:
            print(f"You are {age} years old.")
        else:
            print("Invalid birth year. Please enter a valid year.")
    except TypeError:
        print("Please enter an int")
