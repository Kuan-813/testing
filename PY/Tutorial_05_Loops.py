# TITLE: LOOPS
for i in range(5):
    print(i)

for i in range(1 ,6):
    print(i)

for i in range(0, 10, 2):
    print(i)



# TITLE: WHILE LOOPS
count = 0
while count < 5:
    print(count)
    count += 1



# TITLE: LOOPS CONTROL STATEMENTS
for i in range(1, 10):
    if i == 3:
        continue                        # Skip this iteration
    if i == 7:
        break                           # Exit the loop
    print(i) 



# TITLE: NESTED LOOPS
for i in range(2):
    for j in range(3):
        print(f"{i}, j: {j}")