# Create a dictionary that stores item-cost pairs, and takes input item, and prints cost
# Do error handling: if the item does not exist, print a good error message
fruits = {
    "apple": 10,
    "banana": 20,
    "orange": 30,
}

try:
    a = input("Enter a fruit: ")
    print(fruits[a.lower().strip()])
except KeyError:
    print("Please enter a valid fruit")
