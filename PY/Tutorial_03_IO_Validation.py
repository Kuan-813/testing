# TITLE: INPUT/OUTPUT VALIDATION
name = input("Enter your name: ")
height = float(input("Enter your height: "))                        # Convert to float

# Input:
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Please enter a valid number!")

# Output:
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")



# TITLE: EXERCISE_01
# 1. [SINGLE CALCULATION] Create a simple calculator that takes two numbers and an operator from user.
num1 = float(input("Enter first number: "))                         # Convert to float
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))                        # Convert to float

# Input:
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Output:
print("Result:", result)



# 2. [UNLIMITED CALCULATION - WHILE LOOP] Create a simple calculator that takes two numbers and an operator from user.
while True:
    try:
        num1 = float(input("Enter first number: "))                         # Convert to float
        operator = input("Enter operator (+, -, *, /) or q to quit: ")
        if operator.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break
        num2 = float(input("Enter second number: "))                        # Convert to float

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            
            print("Result:", num1 * num2)
        elif operator == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error! Division by zero.")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Please enter a valid number!")



# TITLE: EXERCISE_02
# 1. Create a simple quiz program with 3 questions. At the end of the quiz, display score.
score = 0
answer1 = input("1. How many colors are there in a rainbow? ")
if answer1.strip() == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 7.")

answer2 = input("2. What do we call a baby cat? ")
if answer2.strip().lower() == "kitten":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is kitten.")

answer3 = input("3. What beans are used to make chocolate? ")
if answer3.strip().lower() == "cocoa":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is cocoa.")

print(f"Your final score is: {score}/3")