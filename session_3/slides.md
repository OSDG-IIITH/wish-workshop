---
title: Bash Scripting Continued
author: OSDG @ IIIT-H
date: 18th October, 2024
---

# Session agenda

## Bash/Linux

- Revision of bash material previous sessions.
- bash: variables, loops, conditionals
- commands like cut, head, tail

---

# Variables

- **Definition**: A way to store data that can be referenced and manipulated.
- **Syntax**:  

```bash
VAR_NAME="value"
echo $VAR_NAME
```

---

# For loops

- **Definition**: To iterate over a list of items.

```bash
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

```bash
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

# Conditionals

- **Purpose**: To control the flow of the script using conditions.

```bash
if [ condition ]; then
    # commands
elif [ condition ]; then
    # commands
else
    # commands
fi
```

---

# Arrays

- **Purpose**: To store multiple values.
```bash
array=(value1 value2 value3)
echo ${array[0]}
arr=("apple" "banana" "cherry")
echo ${arr[1]}  # Output: banana
```

---

# Argument Parsing

- **Purpose**: To handle arguments passed to a script.

```bash
echo "First argument: $1"
echo "Second argument: $2"
```

---

# Functions in Bash

- **Purpose**: To encapsulate and reuse code.

```bash
greet() {
    echo "Hello, $1!"
}
greet "Bash"
```
