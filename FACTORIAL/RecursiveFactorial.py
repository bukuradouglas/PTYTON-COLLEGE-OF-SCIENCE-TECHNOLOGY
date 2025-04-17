#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial_recursive(n):
    if n < 0:
        return "factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# inputint 
n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_recursive(n)}")

