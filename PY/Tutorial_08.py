# TITLE: SETS
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

fruits.add("grape")                            # [add]                              # Output: apple, banana, orange, grape
fruits.remove("banana")                        # [remove]                           # Output: apple, orange
fruits.discard("banana")                       # [remove if exist, no error]

print(fruits)



# TITLE: SET MATHEMATICS OPERATIONS
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))                        # [combine, remove duplicates]       # Output: 1, 2, 3, 4, 5, 6 
print(set1.intersection(set2))                 # [combine, show only duplucates]    # Output: 3, 4
print(set1.difference(set2))                   # [combine, show only difference]    # Output: 1, 2



# TITLE: EXERCISE_01
# 1. Create a system that stores student grades as tuples (name, subject, grade) and
#    uses sets to find unique subjects and students.
grades = [
    ("Alice","Math",85),
    ("Bob","Science",92),
    ("Charlie","Science",78),
    ("Bob","Math",90),
    ("Alice","English",95)
]

students = set()
subjects = set()

for name, subject, grade in grades:
    students.add(name)
    subjects.add(subject)

print("Unique students:", students)            # Output: Unique students: Alice, Bob, Charlie
print("Unique subjects:", subjects)            # Output: Math, Science, English