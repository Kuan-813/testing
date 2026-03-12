# TITLE: FUNCTIONS
# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Kim")                                 # Output: Hello, Kim!

# Function with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)                                       # Output: 8

# Default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Kim"))                      # Output: Hello, Mr. Kim!
print(greet_with_title("Lynette", "Dr."))           # Output: Hello, Dr. Lynette!



# TITLE: AGUMENTS_args
# *args - variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))                       # Output: 15



# TITLE: KEY WORD AGUMENTS_kwargs
# **kwargs - keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Kim", age=18, city="Chicago")      # Output: name: Kim, age: 18, city: Chicago



# TITLE: ARGUMENT & KEY WORD AGUMENTS_args & kwargs
# Combining *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Kim", age=18)      # Output:
                                                    # Positional arguments: (1, 2, 3)
                                                    # Keyword arguments: {'name': 'Kim', 'age': 18}



# TITLE: LAMBDA
# Lambda function - anonymous function
square = lambda x: x ** 2
print(square(5))                                    # Output: 25

add = lambda x, y: x + y
print(add(3, 4))                                    # Output: 7



# TITLE: EXERCISE_01
# 1. Write a function that checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))                                  # Output: True
print(is_prime(10))                                 # Output: False



# TITLE: EXERCISE_02
# 2. Build a temperature converter function that converts Fahrenheit to Celsius. 
#    (Formula: C = (F - 32) * 5/9)
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
print(fahrenheit_to_celsius(77))                    # Output: 25.0