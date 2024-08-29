def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

while True:
    try:
        user_input = input("Enter the grade: ")
        # Check if the input is not empty
        if user_input.strip() == "":
            print("Input cannot be empty. Please enter a valid number.")
            continue
        
        # Try converting the input to float
        grade = float(user_input)
        letter_grade = get_letter_grade(grade)
        print(f"The letter grade is: {letter_grade}")
        break  # Exit the loop after a successful conversion and computation
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

