#!/bin/bash

# Read the number of primes to generate from the user
read -p "Enter the number of prime numbers to generate: " n

# Initialize variables
count=0
num=2

# Loop to find and print the first n primes
while (( count < n )); do
    # Assume the number is prime
    is_prime=1

    # Check if num is prime
    for ((i=2; i*i<=num; i++)); do
        if (( num % i == 0 )); then
            is_prime=0  # Not prime
            break
        fi
    done

    # If the number is prime, print it
    if (( is_prime )); then
        echo "$num"
        ((count++))
    fi

    # Move to the next number
    ((num++))
done
