#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_iterative(n)}")

