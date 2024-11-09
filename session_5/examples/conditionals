## 1. Basic conditional structure
age = 20

if age < 18:
    print("Minor")
elif 18 <= age < 65:
    print("Adult")
else:
    print("Senior")
# Output: Adult


################################################################################

## 2. Ternary conditional

age = 20
category = "Minor" if age < 18 else "Adult"
print(category)  # Output: Adult

#################################################################################

## 3. Logical operators

temperature = 75

# Combining logical operators
is_raining = False
has_umbrella = True

if not is_raining or has_umbrella:
    print("You're good to go outside!")  # Output: You're good to go outside!

##################################################################################

## 4. Pattern matching using match
def get_http_status_message(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"

# Calling the function
print(get_http_status_message(404))  # Output: Not Found


###################################################################################################

## 5. Matching a tuple structure
def identify_shape(shape):
    match shape:
        case ('rectangle', width, height):
            return f"Rectangle of width {width} and height {height}"
        case ('circle', radius):
            return f"Circle with radius {radius}"
        case _:
            return "Unknown shape"

# Testing the function
print(identify_shape(('rectangle', 10, 5)))  # Output: Rectangle of width 10 and height 5
print(identify_shape(('circle', 10, 5)))  # Output: Circle with two args (wrong)
print(identify_shape(('circle', 3)))  # Output: Circle with radius 3

####################################################################################################

## 6. Lazy condition reading in python

l = [1,2,3,4]

# lazy and when false is read
if len(l) > 4 and l[4] == 5:
    print("The fifth element is 5")

q = [1,2,3]
if q and q[1] > 0:
    print("Queue is not empty and has a non zero value")

# lazy or when true is read
if len(l) > 3 or l[4] == 5:
    print("This didn't give an indexing error, length of list is greater than 3")
