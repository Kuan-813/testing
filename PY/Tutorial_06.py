# TITLE: LIST
# fruits = ["apple", "banana", "orange"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["hello", 42, 3.14, True]
# empty_list = []

# print(fruits[0])                                    # Output: apple
# print(fruits[-1])                                   # Output: orange
# print(numbers[1:4])                                 # Output: [2, 3, 4]
# print(numbers[:3])                                  # Output: [1, 2, 3]
# print(numbers[2:])                                  # Output: [3, 4, 5]



# TITLE: LIST OPERATION_CRUD A LIST
# fruits.append("grape")                              # [add to end]                  # Output: apple, banana, orange, grape
# fruits.insert(0, "kiwi")                            # [insert at index]             # Output: kiwi, apple, banana, orange
# fruits.remove("banana")                             # [remove by value]             # Output: apple, orange
# popped = fruits.pop()                               # [remove and return last]      # Output: apple, banana
# fruits.reverse()                                    # [reverse in place]            # Output: orange, banana, apple

# print(fruits)



# TITLE: LIST OPERATIONS
# print(len(fruits))                                  # Output: 3
# print("apple" in fruits)                            # Output: True
# print(fruits + ["mango"])                           # Output: apple, banana, orange, mango
# print(fruits * 2)                                   # Output: apple, banana, orange, apple, banana, orange



# TITLE: EXERCISE_01
# 1. Create a grocery list and perform various operations.
grocery_list = ["flour", "bread", "eggs"]

# add item:
grocery_list.append("butter")
grocery_list.insert(2, "sugar")

# remove item:
grocery_list.remove("eggs")
popped_item = grocery_list.pop(1)

# search and sort
if "bread" in grocery_list:
    print(f"Found bread! Total items: {len(grocery_list)}")

grocery_list.sort()

# display final list
print("\nFinal Grocery List:")
for index, item in enumerate(grocery_list, start =1):
    print(f"{index}.{item}")



# TITLE: EXERCISE_02
# 2. Write a program that finds the largest and smallest number in list.
# METHOD 1
numbers = [68, 6, 96, -6, 138, 87]

largest = max(numbers)
smallest = min(numbers)

print(f"Largest Number: {largest}, Smallest Number: {smallest}")

# METHOD 2
numbers = [68, 6, 96, -6, 138, 87]

# Initialize with the first element of the list
max_num = min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"Largest Numnber: {max_num}, Smallest Number: {min_num}")