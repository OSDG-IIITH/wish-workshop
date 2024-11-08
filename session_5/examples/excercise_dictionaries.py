# 1. Create a dictionary that maps each letter in a string to the number of times it appears.
# If the string is 'mississippi', the output should be: {'m': 1, 'i': 4, 's': 4, 'p': 2}
































# Solution
def letter_frequency(string):
    frequency = {}
    for letter in string:
        frequency[letter] = frequency.get(letter, 0) + 1
    return frequency

print(letter_frequency("mississippi"))



#################################################################################################





# 2. Given two dictionaries, combine them by adding values for keys that appear in both.
# For example: {'a': 1, 'b': 2} and {'b': 3, 'c': 4} should result in {'a': 1, 'b': 5, 'c': 4}
































# Solution
def combine_dictionaries(dict1, dict2):
    combined = dict1.copy()
    for key, value in dict2.items():
        combined[key] = combined.get(key, 0) + value
    return combined

print(combine_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


####################################################################################################3


# 3. Write a function to reverse a dictionary.
# For example, given {'a': 1, 'b': 2, 'c': 3}, it should return {1: 'a', 2: 'b', 3: 'c'}





























# Solution
def reverse_dictionary(d):
    return {value: key for key, value in d.items()}

print(reverse_dictionary({'a': 1, 'b': 2, 'c': 3}))



#####################################################################################################


# 4. Given a dictionary with nested dictionaries, write a function to flatten it.
# Each key in the output should be a string representing the path to the key in the original dictionary.
# For example: {'a': {'b': {'c': 1}}} should become {'a.b.c': 1}

# Solution
def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

print(flatten_dict({'a': {'b': {'c': 1}}}))


# 5. Write a function to find the most frequent value in a dictionary.
# For example, given {'a': 3, 'b': 2, 'c': 3, 'd': 4}, it should return 3.

# Solution
from collections import Counter

def most_frequent_value(d):
    values = list(d.values())
    return max(values)

print(most_frequent_value({'a': 3, 'b': 2, 'c': 3, 'd': 4}))


# 6. Create a dictionary comprehension that maps each character in a string to its index.
# If a character appears multiple times, it should store only the last index.
# Example: For "banana", the dictionary should be {'b': 0, 'a': 5, 'n': 4}

# Solution
def last_index_map(string):
    return {char: i for i, char in enumerate(string)}

print(last_index_map("banana"))


# 7. Write a function to merge multiple dictionaries, with values being lists.
# If a key appears in multiple dictionaries, combine all values into a single list.
# Example: [{'a': 1}, {'a': 2, 'b': 3}, {'a': 4, 'b': 5, 'c': 6}] should become {'a': [1, 2, 4], 'b': [3, 5], 'c': [6]}

# Solution
def merge_dicts_with_lists(dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            merged.setdefault(key, []).append(value)
    return merged

print(merge_dicts_with_lists([{'a': 1}, {'a': 2, 'b': 3}, {'a': 4, 'b': 5, 'c': 6}]))


# 8. Create a function that takes a dictionary and returns the keys with the top N highest values.
# Example: For {'a': 1, 'b': 4, 'c': 3}, top 2 keys should be ['b', 'c']

# Solution
def top_n_keys(d, n):
    return sorted(d, key=d.get, reverse=True)[:n]

print(top_n_keys({'a': 1, 'b': 4, 'c': 3}, 2))

