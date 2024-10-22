#!/bin/bash

# question 1
echo "Question1:"

a=$((16 + 2)) # what is the output
b=[[16+2]]
echo "a is: " $a
echo "b is: " $b

# question 2
echo "Question2:"

[ -f *.txt ]
echo "return val with * is: " $?

[[ -f file.txt ]]
echo "return val without * is: " $?

# question 3
echo "Question3:"

[[ -f *.txt ]]
echo "return val without: " $?

# question 4
echo "Question4:"

fruit=banana
echo "fruitification output: " $fruitification
echo "fruit output: " ${fruit}ification

# question 5
echo "Question5:"
echo {01..10}
echo {01..20..3}
