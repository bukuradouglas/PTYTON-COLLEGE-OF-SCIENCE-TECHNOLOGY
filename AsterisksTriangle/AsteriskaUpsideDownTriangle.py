#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def triangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)

n = int(input("Enter the size of the triangle: "))
triangle(n)

