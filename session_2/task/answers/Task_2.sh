#!/bin/bash

# 1
cal -1 > output1.txt

# 2
date +%Y-%m-%d >> output1.txt

# 3
for (( i=0; i<100; i++ )) 
do 
    echo "ISS is cool" >> output1.txt
done

# 4
cat output1.txt

# 5
head -3 output1.txt

# 6
head -15 output1.txt | tail +6

# 7
cat output1.txt | wc -l

# 8
echo "I'm UG1" >> output1.txt

# 9
wc -w output1.txt

# 10
echo "I'm studying ISS" >> output1.txt

# 11
cut -d' ' -f4 output1.txt

# 12
awk '{print $2, $3, $4, $5}' output1.txt

# 13
cut -f 3 -d' ' output1.txt | head -n $(($(wc -l < output1.txt) -5)) output1.txt

# 14
awk '{print $2, $4}' output1.txt


