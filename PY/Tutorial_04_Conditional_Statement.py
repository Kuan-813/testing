# TITLE: CONDITIONAL STATEMENTS_IF, ELIF, ELSE
# Example 1 - Simple if statement
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2 - If-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")



# TITLE: CONDITIONAL STATEMENTS_AND, OR
# Example 1 - Using AND operator
user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You are allowed to drive.") 
else:
    print("You are not allowed to drive.") 

# Example 2 - Using OR operator
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")



# TITLE: CONDITIONAL STATEMENTS_NESTED IF
weather = "sunny"
temperature = 75

if weather == "sunny":
    if temperature > 70:
        print("It's sunny and warm!")
    else:
        print("It's sunny but cool.")



# TITLE: EXERCISE_01
# 1. Write a program that cateforizes BMI (Body Mass Index) into underweight (,18.5),
#    normal weight (<24.9), overweight (<29.9), and obesity (<30.0).
#    Formula = kg/m^2)
weight = float(input("Enter your weight in kg: "))                      # Convert to float
height = float(input("Enter your height in meters: "))                  # Convert to float

bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is {bmi:.2f} and you are categorized as {category}.")