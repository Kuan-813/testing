# TITLE: CLASSES AND OBJECTS
# Basic class definition
class Person:
    # Class attribute(shared by all instances)
    species = "Homo sapiens"

    # Constructor method
    def __init__(self, name, age):
        # Instnace attributes
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! {self.name} is now {self.age}."

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)                                 # Output: Alice
print(person1.age)                                  # Output: 25
print(person2.name)                                 # Output: Bob
print(person2.age)                                  # Output: 30    

# Calling instance methods
print(person1.introduce())                          # Output: Hi, I'm Alice and I'm 25 years old.
print(person2.introduce())                          # Output: Hi, I'm Bob and I'm 30 years old.
print(person1.have_birthday())                      # Output: Happy Birthday! Alice is now 26.
print(person2.have_birthday())                      # Output: Happy Birthday! Bob is now 31.

# Class attributes
print(Person.species)                               # Output: Homo sapiens
print(person1.species)                              # Output: Homo sapiens
print(person2.species)                              # Output: Homo sapiens