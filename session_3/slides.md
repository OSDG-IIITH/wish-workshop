---
author: OSDG @ IIIT-H
date: 18th October, 2024
title: Bash Scripting Continued
---

# Session agenda

## Bash/Linux

- Revision of bash material previous sessions.
- bash: variables, loops, conditionals
- commands like cut, head, tail

---

# Variables

- **Definition**: A way to store data that can be referenced and
  manipulated.
- **Syntax**:

``` bash
VAR_NAME="value"
echo $VAR_NAME
```

---

## Basic Variable Access with `${}`

- **Purpose**: To explicitly refer to the value of a variable.
- **Example**:
  ``` bash
  name="Bash"
  echo "Hello, ${name}!"  # Output: Hello, Bash!
  ```

---

## `()` - Command Grouping and Subshells

- **Purpose**:

  - To group commands or create a subshell where variables and changes
    don't affect the parent shell.

- **Example**:

  ``` bash
  (cd /tmp && echo "Now in /tmp")
  pwd  # Still in the original directory
  ```

---

## `(())` - Arithmetic Expansion

- **Purpose**:

  - Used for performing arithmetic operations in Bash.

- **Example**:

  ``` bash
    num=5
    ((num++))
    echo $num  # Output: 6
  ```

---

## `$(())` - Arithmetic Expansion

- **Purpose**:

  - Used to perform arithmetic operations and return the result.

- **Example**:

  ``` bash
    result=$((5 + 3))
    echo $result  # Output: 8
  ```

---

## `$()` - Command Substitution

- **Purpose**:

  - Used to capture the output of a command and use it as a value for a
    variable or in another command.

- **Example**:

  ``` bash
    current_dir=$(pwd)
    echo "You are in $current_dir"
  ```

---

# Conditionals

- **Purpose**: To control the flow of the script using conditions.

``` bash
if [ condition ]; then
    # commands
elif [ condition ]; then
    # commands
else
    # commands
fi
```

---

# Conditionals: Example 1

``` bash
num=10
if [ $num -gt 5 ]; then
    echo "Number is greater than 5"
else
    echo "Number is 5 or less"
fi
```

- `-gt`: greater than. `-ge`: greater than or equal
- `-lt`: less than. `-le`: less than or equal
- `-eq`: equal. `-ne`: not equal

---

# Conditionals: Example 2

``` bash
name="Bash"
if [ "$name" == "Bash" ]; then
    echo "This is Bash"
else
    echo "This is not Bash"
fi
```

- `==`: equal. `!=`: not equal
- `-z`: string is null (has zero length). `-n`: string is not null

---

# Conditionals: Example 3

``` bash
file="test.txt"
if [ -f "$file" ]; then
    echo "$file exists"
else
    echo "$file does not exist"
fi
```

- `-f`: file exists and is a regular file. `-d`: file exists and is a
  directory
- `-r`: file is readable. `-w`: file is writable. `-x`: file is
  executable

---

# Conditionals: Example 4

- AND condition

``` bash
num1=10
num2=20
if [ $num1 -lt 15 ] && [ $num2 -gt 15 ]; then
    echo "Both conditions are true"
fi
```

- OR condition

``` bash
if [ $num1 -lt 5 ] || [ $num2 -gt 15 ]; then
    echo "At least one condition is true"
fi
```

---

# Conditionals: Example 5

``` bash
num=5
if ! [ $num -gt 10 ]; then
    echo "Number is not greater than 10"
fi
```

---

# For loops

- **Definition**: To iterate over a list of items.

``` bash
for item in list; do
    echo "Item $item"
done
for i in {1..5}; do
    echo "Loop $i"
done
```

---

# While loops

- **Purpose**: Executes a block of code as long as a condition is true.

``` bash
while [ condition ]; do
    # commands
done
counter=1
while [ $counter -le 5 ]; do
    echo "Count $counter"
    ((counter++))
done
```

---

# Arrays

- **Purpose**: To store multiple values.

``` bash
array=(value1 value2 value3)
echo ${array[0]}
arr=("apple" "banana" "cherry")
echo ${arr[1]}  # Output: banana
```

---

# Argument Parsing

- **Purpose**: To handle arguments passed to a script.

``` bash
echo "First argument: $1"
echo "Second argument: $2"
```

---

# Functions in Bash

- **Purpose**: To encapsulate and reuse code.

``` bash
greet() {
    echo "Hello, $1!"
}
greet "Bash"
```

---

# Contact us

If you have any doubts, or have to inform us something, please feel free
to reach out to us through email:

- Abhiram Tilak (<abhiram.potula@research.iiit.ac.in>)
- Ankith Pai (<ankith.pai@research.iiit.ac.in>)
- Praneeth Jain (<moida.praneeth@students.iiit.ac.in>)

## Reference Material


It is good to link to material which is much better and more organized:

- Distrotube:
  https://youtube.com/playlist?list=PL5--8gKSku174EnRTbP4DzU2W80Q1vqtm>
