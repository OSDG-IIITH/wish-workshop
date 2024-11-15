try:
    a = int(input("Enter a value: "))
    print(a)
except ValueError:
    print("Please enter a number")

try:
    a = int(input("Enter a value: "))
    print(1 / a)
except ValueError as a:
    print("Please enter a number", a)
except ZeroDivisionError:
    print("Please don't enter 0")
else:
    print("Done")
