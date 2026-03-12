# TITLE: LOOPS
# TITLE: EXERCISE_01
# 1. Create a multiplication table generator.
# METHOD 1
num = int(input("Enter the number for the table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * 1}")


# METHOD 2
print("Full Multiplication Table (1-10):")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()


# METHOD 3
# Defining size of the table
size = 10

# Printing header row
print("     ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (size * 4 + 5))

# Generate row
for row in range(1, size + 1):
    print(f"{row:2} |", end="")
    for col in range(1, size + 1):
        print(f"{row * col:4}", end="")
    print()


# METHOD 4
def generate_table():
    try:
        num = int(input("Enter the number for the table: "))
        limit = int(input("Enter the limit (e.g., 12): "))

        print(f"\nMultiplication Table for {num}:")
        for i in range (1, limit + 1):
            print(F"{num} x {i:2} = {num * i}")
    except ValueError:
        print("Please enter valid number!")

generate_table()



# TITLE: EXERCISE_02
# 2. Write a program that finds all prime numbers up to a given number. (limit = 20)
limit = 20

primes = [n for n in range(2, limit + 1)
          if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print(f"Prime numbers up to {limit}: {primes}")