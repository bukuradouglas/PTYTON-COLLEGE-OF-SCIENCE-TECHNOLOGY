#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to the square root of n
        if n % i == 0:
            return False
    return True

# Get user input
n = int(input("Please enter an integer: "))

# Check if the number is prime
if is_prime(n):
    print(f"{n} is prime.")

else:
    print(f"{n} is not prime.")

