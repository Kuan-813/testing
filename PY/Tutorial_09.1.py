# TITLE: DICTIONARIES
# TITLE: EXERCISE_01
# 1. Create a dictionary called student_records with the following informaiton:
#    "student_001": name is "John", age is 19, major is "Computer Science", grades are [85, 92, 78].
#    "student_002": name is "Sarah", age is 20, major is "Biology", grades are [90, 88, 95].
# 2. Add a new student "student_003" with name "Mike", age 18, major "Math", grades [82, 79, 91].
# 3. update John's age to 20.
# 4. Loop through the dictionary and print each student's information in this format:
#    "Stident ID: [id], Name: [Name], Major: [major]".
student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    },
    "student_003": {
        "name": "Mike",
        "age": 18,
        "major": "Math",
        "grades": [82, 79, 91]
    }
}

student_records["student_001"]["age"] = 20
print(student_records)

for student_id, info in student_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")