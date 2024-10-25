""" Lists """

# Different ways to check variable types in Python

# Using type() function - returns the type class of the variable
# Basic Types
number_integer = 42
number_float = 3.14
text_string = "Hello, World!"
is_boolean = True
none_value = None

print("=== Basic Types ===")
print(f"Integer: {type(number_integer)}")  # <class 'int'>
print(f"Float: {type(number_float)}")      # <class 'float'>
print(f"String: {type(text_string)}")      # <class 'str'>
print(f"Boolean: {type(is_boolean)}")      # <class 'bool'>
print(f"None: {type(none_value)}")         # <class 'NoneType'>

# Collection Types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

print("\n=== Collection Types ===")
print(f"List: {type(my_list)}")           # <class 'list'>
print(f"Tuple: {type(my_tuple)}")         # <class 'tuple'>
print(f"Set: {type(my_set)}")             # <class 'set'>
print(f"Dictionary: {type(my_dict)}")     # <class 'dict'>

# Using isinstance() function - checks if object is of a specific type
print("\n=== Using isinstance() ===")
print(f"Is 42 an integer? {isinstance(number_integer, int)}")        # True
print(f"Is 'Hello' a string? {isinstance(text_string, str)}")        # True
print(f"Is [1,2,3] a list? {isinstance(my_list, list)}")            # True

# Multiple type checking with isinstance()
print(f"Is 3.14 an int or float? {isinstance(number_float, (int, float))}")  # True

# Custom Class example
class MyClass:
    pass

my_object = MyClass()
print("\n=== Custom Class ===")
print(f"Custom object: {type(my_object)}")  # <class '__main__.MyClass'>
print(f"Is it MyClass? {isinstance(my_object, MyClass)}")  # True

# Special number types
complex_num = 1 + 2j
binary_num = 0b1010
hex_num = 0xFF

print("\n=== Special Number Types ===")
print(f"Complex: {type(complex_num)}")     # <class 'complex'>
print(f"Binary: {type(binary_num)}")       # <class 'int'>
print(f"Hexadecimal: {type(hex_num)}")     # <class 'int'>

# Type checking in Python 3.5+ using typing module
from typing import List, Dict

typed_list: List[int] = [1, 2, 3]
typed_dict: Dict[str, int] = {"a": 1, "b": 2}

print("\n=== Type Hints (for documentation) ===")
print(f"Typed list: {type(typed_list)}")   # Still returns <class 'list'>
print(f"Typed dict: {type(typed_dict)}")   # Still returns <class 'dict'>