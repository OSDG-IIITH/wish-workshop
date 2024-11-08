# Loops and iterations in python

## 1. For loop iterating over a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# While loop with a simple condition
count = 3
while count > 0:
    print(count)
    count -= 1
# Output: 3, 2, 1


###########################################################################################


## 2. Using range to loop a specific number of times

for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Using range with start, stop, and step
for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9


#########################################################################################


## 3. Using else with a loop to find a specific item

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Found 3!")
        break
else:
    print("3 was not found")
# Output: Found 3!

# Example when 3 is not in the list
numbers = [1, 2, 4, 5]

for num in numbers:
    if num == 3:
        print("Found 3!")
        break
else:
    print("3 was not found")
# Output: 3 was not found


####################################################################################


## 4. List comprehension to create a list of squares

squares = [x**2 for x in range(6)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25]

# List comprehension with condition
even_squares = [x**2 for x in range(6) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16]

# Generator expression (creates an iterator)
squares_gen = (x**2 for x in range(6))
print(next(squares_gen))  # Output: 0
print(next(squares_gen))  # Output: 1
# Generators don't store values in memory and are computed on-the-fly
