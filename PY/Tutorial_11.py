# TITLE: ERROR HANDLING
# Basic error handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Using else and finally
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    # Excecute if no exception occurred
    content = file.read()
    print("File read successfully")
finally:
    # Always excecutes
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup completed.")

# Raising exceotions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
