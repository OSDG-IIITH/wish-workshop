# dictionaries 

## 1. Book example

book = {
    'title': 'The House of Mirth',
    'author': 'Edith Wharton',
    'year': 1960
}

print(book['title'])
print(book['author'])

######################################################################


## 2. Creating a dictionary with mixed data types
person = {
    'name': 'Alice',
    'age': 28,
    'hobbies': ['reading', 'cycling', 'painting'],
    'address': {
        'city': 'New York',
        'zip': '10001'
    }
}

### Accessing nested dictionary and list items

print(person['name'])            
print(person['hobbies'][1])      
print(person['address']['city']) 


##################################################################################


## 3. Adding a new key-value pair
person['profession'] = 'Engineer'

### Updating an existing key
person['age'] = 29

print(person)


##################################################################


## 4. Using get to access keys that may or may not exist
print(person.get('age', 'Not specified'))    # Output: 29
print(person.get('nationality', 'Unknown'))  # Output: Unknown


#######################################################################3


## 5. Iterating through a dictionary

### Looping through keys
for key in person:
    print(key)  # Output: name, age, hobbies, address, profession

### Looping through values
for value in person.values():
    print(value)

### Looping through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")


#############################################################################


## 6. Deleting entries

### Deleting a key-value pair
del person['profession']

### Using pop to remove a key and get its value
age = person.pop('age')
print(age)      # Output: 29

### Clearing the dictionary
person.clear()
print(person)   # Output: {}


#########################################################################

## 7. Counting occurrences of each word in a list

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}


#########################################################################

## 8. Creating a dictionary where keys are numbers and values are their squares

squares = {num: num**2 for num in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

