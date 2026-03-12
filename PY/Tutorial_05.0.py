# TITLE: LOOPS
for i in range(5):
    print(i)                                # Output: 0, 1, 2, 3, 4

for i in range(1 ,6):
    print(i)                                # Output: 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)                                # Output: 0, 2, 4, 6, 8



# TITLE: WHILE LOOPS
count = 0
while count < 5:
    print(count)                            # Output: 0, 1, 2, 3, 4
    count += 1



# TITLE: LOOPS CONTROL STATEMENTS
for i in range(1, 10):
    if i == 3:
        continue   
        # Skip this iteration
    if i == 7:
        break
        # Exit the loop
    print(i)                                # Output: 1, 2, 3, 4, 5, 6



# # TITLE: NESTED LOOPS
for i in range(2):
    for j in range(3):
        print(f"{i}, j: {j}")               # Output: 0, j: 0
                                            # Output: 0, j: 1
                                            # Output: 0, j: 2
                                            # Output: 1, j: 0
                                            # Output: 1, j: 1
                                            # Output: 1, j: 2