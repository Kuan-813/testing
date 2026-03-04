grades = [
    ("Alice","Match",85),
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

print("Unique students:", students)
print("Unique subjects:", subjects)