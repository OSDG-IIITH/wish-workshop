# Methods in Python

## 1. Basic function that adds two numbers
def add(a, b):
    return a + b

# Calling the function
result = add(3, 5)
print(result)  # Output: 8


##################################################################################


## 2. Function with default parameter for greeting
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Calling the function with and without the second argument
print(greet("Alice"))           # Output: Hello, Alice!
print(greet("Alice", "Hi"))     # Output: Hi, Alice!


###################################################################################


## 3. Function that formats an address
def format_address(city, state, zip_code):
    return f"{city}, {state} {zip_code}"

# Calling the function with keyword arguments
print(format_address(city="New York", state="NY", zip_code="10001"))
# Output: New York, NY 1000


##################################################################################


## 4. Function that sums any number of arguments
def sum_all(*args):
    return sum(args)

# Calling the function with multiple arguments
print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5, 10, 15))   # Output: 30


################################################################################


## 5. Function that prints personal information

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with multiple keyword arguments
display_info(name="Alice", age=30, city="New York")

# Output:
# name: Alice
# age: 30
# city: New York


###########################################################################


## 6. Function that applies a given function to a number

def apply_func(func, value):
    return func(value)

def square(value):
    return value**2

# Calling with different functions
print(apply_func(square, 5))   # Output: 25


#################################################################################

## 7. Function that returns a function

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

# Getting a function that prints "Hello"
hello_func = outer_function("Hello")
hello_func()  # Output: Hello
