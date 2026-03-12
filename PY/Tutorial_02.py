# TITLE: INDEXING AND SLICING
text = "Python Programming"

print(text[0])                                                            # [first character]     # Output: P     
print(text[-1])                                                           # [last character]      # Output: g
print(text[0:6])                                                          # [slice 0 to 5]        # Output: Python
print(text[:6])                                                           # [from start to 5]     # Output: Python
print(text[7:17])                                                         # [from 7 to 17]        # Output: Programming



# TITLE: STRING METHODS
name = "bob the builder"

print(len(name))                                                          # [length]              # Output: 15
print(name.strip())                                                       # [remove whitespace]   # Output: bob the builder
print(name.upper())                                                       # [upper case]          # Output: BOB THE BUILDER
print(name.lower())                                                       # [lower case]          # Output: bob the builder 
print(name.title())                                                       # [title case]          # Output: Bob The Builder
print(name.replace("bob", "kim"))                                         # [replace]
print(name.find("the"))                                                   # [find substring]      # Output: 4
print("the" in name)                                                      # [check substring]     # Output: True (case sensitive)
print("The" in name)                                                      # [check substring]     # Output: False (case sensitive)
print("fisherman" not in name)                                            # [check substring]     # Output: True



# TITLE: STRING FORMATTINGS
name = "Kimmie"
age = 18

message_1 = f"My name is {name} and I am {age} years old."                # [f-string]
message_2 = "My name is {} and I am {} years old.".format(name, age)      # [str.format()]
message_3 = "My name is %s and I am %d years old." % (name, age)          # [%-formatting]

print(message_1)                                                          # Output: My name is Kimmie and I am 18 years old.
print(message_2)                                                          # Output: My name is Kimmie and I am 18 years old.
print(message_3)                                                          # Output: My name is Kimmie and I am 18 years old.



# TITLE: EXERCISE_01
# 1. Build a simple text analyzer that counts words, characters, and sentences in a given text,
import string

text = """Python is a powerful programming language.
It's easy to learn and versatile!
You can use python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

char_count = len(text)                                                    # [count characters, including spaces and punctuation]
words = text.split()                                                      # [split text by whitespace, into list of words]
word_count = len(words)                                                   # [count words, split by whitespace]
sentence_count = text.count('.') + text.count('!') + text.count('?')      # [count sentences, based on punctuation]
clean_text = text.translate(str.maketrans('', '', string.punctuation))    # [remove punctuation from text]       # NOTE: variable [words = text.split()] MUST APPEAR BEFORE variable [word_count = len(words)]
clean_text = clean_text.lower()                                           # [convert text to lower case]
python_count = words.count("python")                                      # [count occurrences of "python", case-sensitive]
Python_count = words.count("Python")                                      # [count occurrences of "Python", case-sensitive]
longest_word = max(words, key=len)                                        # [find longest word, based on length] 
shortest_word = min(words, key=len)                                       # [find shortest word, based on length]
total_length = sum(len(word) for word in words)                           # [calculate total length of all words]
average_word_length = total_length / word_count                           # [calculate average word length]  

print(f"Character count: {char_count}")                                   # Output: Character count: 239
print(f"Word count: {word_count}")                                        # Output: Word count: 38
print(f"Sentence count: {sentence_count}")                                # Output: Sentence count: 5
print(f"Clean word count: {len(words)}")                                  # Output: Clean word count: 38
print(f"Occurrence of 'python': {python_count}")                          # Output: Occurrence of 'python': 1
print(f"Occurrence of 'Python': {Python_count}")                          # Output: Occurrence of 'Python': 2
print(f"Longest word: {longest_word}")                                    # Output: Longest word: development,   # NOTE: it will be "programming" if punctuation is removed before this variable
print(f"Shortest word: {shortest_word}")                                  # Output: Shortest word: a
print(f"Average word length: {round(average_word_length, 2)}")            # Output: Average word length: 5.32