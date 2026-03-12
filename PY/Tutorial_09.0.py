# TITLE: DICTIONARIES
student = {
    "name": "Alice",
    "age": 18,
    "grade": "A+",
    "courses": ["Math", "Science", "English"]
}

print(student["name"])                                                  # Output: "Alice"
print(student.get("age"))                                               # Output: 18
student["age"] = 25
print(student["age"])                           # [modify value]        # Output: 25
student["email"] = "alice@gmail.com"
print(student["email"])                         # [add new key-value]   # Output: alice@gmail.com



# TITLE: DICTIONARIES METHOD
keys = student.keys()                           # [get all keys]
values = student.values()                       # [get all values]
items = student.items()                         # [get key-value pairs]

print(keys)                                                             # Output: dict_keys(['name', 'age', 'grade', 'courses', 'email'])
print(values)                                                           # Output: dict_values(['Alice', 18, 'A+', ['Math', 'Science', 'English'], 'alice@gmail.com'])
print(items)                                                            # Output: dict_items([('name', 'Alice'), ('age', 25), ('grade', 'A+'), ('courses', ['Math', 'Science', 'English']), ('email', 'alice@gmail.com')])



# TITLE: ITERATING DICTIONARIES
for key in student:                                                     # Output: name: Alice
    print(f"{key}: {student[key]}")                                     #         age: 18
                                                                        #         grade: A+
for key, value in student.items():                                      #         courses: ['Math', 'Science', 'English']
    print(f"{key}: {value}")                                            #         email: alice@gmail.com



# TITLE: NESTED DICTIONARIES
company = {
    "employees": {
        "John": {"age":30 , "department": "IT"},
        "Alice": {"age": 25, "department": "HR"}
    },
    "departments": ["IT", "HR", "Fiannce"]
}

print(company["employees"].items())                                    # Output: dict_items([('John', {'age': 30, 'department': 'IT'}), ('Alice', {'age': 25, 'department': 'HR'})])
print(company["departments"])                                          # Output: ['IT', 'HR', 'Fiannce']